from flask import Flask, Response
import requests
from lxml import etree

app = Flask(__name__)

@app.route('/meteogram')
def serve_modified_svg():
    url = 'https://www.yr.no/nb/innhold/1-92416/meteogram.svg'
    response = requests.get(url)

    if response.status_code != 200:
        return "Failed to fetch SVG", 500

    parser = etree.XMLParser()
    root = etree.fromstring(response.content, parser)

    # List of transform values to remove
    transforms_to_remove = {
        'translate(30 180)',
        'translate(30 252)',
        'translate(30, 278)',  # Note: comma version
    }

    ns = {'svg': 'http://www.w3.org/2000/svg'}
    g_elements = root.findall('.//svg:g', namespaces=ns)

    # Collect and remove matching <g> elements
    for g in g_elements:
        transform = g.get('transform')
        if transform in transforms_to_remove:
            parent = g.getparent()
            parent.remove(g)

    modified_svg = etree.tostring(root, encoding='utf-8', xml_declaration=True)
    return Response(modified_svg, mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
