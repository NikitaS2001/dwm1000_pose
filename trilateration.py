import math
import numpy
import scipy

class Trilateration:

    """Solution of the trilateration problem
    in the form of a system of nonlinear equations
    using global optimization methods"""

    __bases_coord: dict
    __base_dist: dict

    def __init__(self, base_coord: dict) -> None:
        self.__bases_coord = base_coord
    
    def set_bases_coord(self, base_coord: dict) -> None:
        self.__bases_coord = base_coord

    def get_bases_coord(self, base_coord: dict) -> dict:
        return self.__bases_coord

    def solvelm(self, base_dist :dict, guess: numpy.array) -> numpy.array:
        """ Return a numpy.array [x, y, z]

        Solves the system of nonlinear equations in a least squares sense 
        using a modification of the Levenberg-Marquardt algorithm
        """
        self.__base_dist = base_dist
        # return scipy.optimize.root(self.__fun, guess, method="lm").x
        return scipy.optimize.root(self.__fun, guess, jac=self.__jac, method="lm").x

    def __jac(self, v):
        """ Return function

        Creation of the Jacobian matrix
        """
        f = numpy.zeros([len(self.__base_dist.keys()), 3])
        for i, base in enumerate(self.__base_dist):
            for j in range(len(self.__bases_coord.values()[0])):
                f[i][j] = 2*(v[j]-self.__bases_coord.get(base)[j])
        return f

    def __fun(self, v):
        """ Return function

        Creation of a system of nonlinear equations        
        """
        f = numpy.zeros([len(self.__base_dist)])
        for i, base in enumerate(self.__base_dist):
            f[i] = math.pow(v[0]-self.__bases_coord.get(base)[0], 2) \
                 + math.pow(v[1]-self.__bases_coord.get(base)[1], 2) \
                 + math.pow(v[2]-self.__bases_coord.get(base)[2], 2) \
                 - math.pow(self.__base_dist.get(base), 2)
        return f