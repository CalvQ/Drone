from smbus2 import SMBus
import numpy as np
import math

#bus = SMBus(1)    

def isclose(x, y, rtol=1.e-5, atol=1.e-8):
    return abs(x-y) <= atol + rtol * abs(y)

def eulerAngle(R):
    phi = 0.0
    if isclose(R[2,0],-1.0):
        theta = math.pi/2.0
        psi = math.atan2(R[0,1],R[0,2])
    elif isclose(R[2,0],1.0):
        theta = -math.pi/2.0
        psi = math.atan2(-R[0,1],-R[0,2])
    else:
        theta = -math.asin(R[2,0])
        cos_theta = math.cos(theta)
        psi = math.atan2(R[2,1]/cos_theta, R[2,2]/cos_theta)
        phi = math.atan2(R[1,0]/cos_theta, R[0,0]/cos_theta)
    return psi, theta, phi

def rotation_matrix(ax, ay, az, bx, by, bz):
    a = np.array([ax, ay, az])
    a = a/np.linalg.norm(a)
    '''
    #magnitudeA = (ax**2 + ay**2 + az**2)**0.5
    magnitudeA = np.linalg.norm(np.array([ax, ay, az]))
    a = np.array([ax/magnitudeA, ay/magnitudeA, az/magnitudeA])
    '''

    b = np.array([bx, by, bz])
    b = b/np.linalg.norm(b)
    '''
    #magnitudeB = (bx**2 + by**2 + bz**2)**0.5
    magnitudeB = np.linalg.norm(np.array([bx, by, bz]))
    b = np.array([bx/magnitudeB, by/magnitudeB, bz/magnitudeB])
    '''
    
    angle = np.arccos(np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b)))

    v = np.cross(a, b)
    s = np.linalg.norm(v)*np.sin(angle)
    c = np.dot(a, b)*np.cos(angle)

    identity = np.identity(3)
    
    vcross = np.array([
                       [0, -v[2], v[1]],
                       [v[2], 0, -v[0]],
                       [-v[1], v[0], 0]])

    constant = 1/(1+c)
    
    matrix =np.array([
              [0.0,0.0,0.0],
              [0.0,0.0,0.0],
              [0.0,0.0,0.0]])
    matrix = np.add(matrix, identity)
    matrix = np.add(matrix, vcross)
    matrix = np.add(matrix, (np.square(vcross) * constant))

    print matrix
    return matrix
    '''
    for i in range(len(matrix)/3):
        for j in range(len(matrix[i])):
            matrix[i][j] += identity[i][j]
            matrix[i][j] += vcross[i][j]
            matrix[i][j] += (np.square(vcross) * constant)
    
    print matrix
    theta = 0.0
    psi = 0.0
    phi = 0.0
            
    if abs(matrix[2][0]) != 1:
        theta = -np.arcsin(matrix[2][0])
        psi = np.arctan2((matrix[2][1]/np.cos(theta)), (matrix[2][2]/np.cos(theta)))
        phi = np.arctan2((matrix[1][0]/np.cos(theta)), (matrix[0][0]/np.cos(theta)))
    else:
        if matrix[2][0]==-1:
            theta = math.pi/2
            psi = np.arctan2(matrix[0][1], matrix[0][2])
        else:
            theta = -math.pi/2
            psi = np.arctan2(-matrix[0][1], -matrix[0][2])

    out = np.array([psi, theta, phi])
    #this is in rotations of x, y, z
    #psi, theta, phi

    rad_to_deg = 180/math.pi

    print out*rad_to_deg
    '''
    

print eulerAngle(rotation_matrix(1,2,3,4,5,6))
