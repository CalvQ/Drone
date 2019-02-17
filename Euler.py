from smbus import SMBus
import numpy as np

bus = SMBus(1)    

def skew_symmetric_cross(a, b, c):
    temp = np.cross(b,c)
    temp[0] = temp[0]*a[0]
    temp[1] = temp[1]*a[1]
    temp[2] = temp[2]*a[2]
    return temp

def rotation_matrix(ax, ay, az, bx, by, bz):
    magnitudeA = (ax**2 + ay**2 + az**2)**0.5
    a = np.array([ax/magnitudeA, ay/magnitudeA, az/magnitudeA])
    magnitudeB = (bx**2 + by**2 + bz**2)**0.5
    b = np.array([bx/magnitudeB, by/magnitudeB, bz/magnitudeB])

    angle = np.arccos(np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b)))
    
    v = np.cross(a, b)
    s = np.linalg.norm(v)*np.sin(angle)
    c = np.dot(a, b)*np.cos(angle)

    identity = np.array([[1,0,0],[0,1,0],[0,0,1]])
    vcross = skew_symmetric_cross(x=[0, -1*v[2], v[1]],
                                  y=[v[2], 0, -1*v[0]],
                                  z=[-1*v[1], v[0], 0])

    constant = 1/(1+c)
    
    out = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(len(out)):
        for j in range(len(a[i])):
            out += identity[i][j]
            out += vcross[i][j]
            out += (np.square(vcross) * constant)

    return out


print rotation_matrix(1,1,1,0,0,-1)
