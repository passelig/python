
from roboticstoolbox import ET2
import numpy as np


arm1 = 3;
arm2 = 2;
robot = ET2.R() * ET2.tx(arm1)* ET2.R() * ET2.tx(arm2);

robot.plot(np.deg2rad([70,-130]));
