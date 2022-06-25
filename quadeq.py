# import complex math module  
from numpy import emath, meshgrid, linspace
import matplotlib.pyplot as plt
class QuadraticEquation(object):
    """
    A quadratic equation of the form a*x*x + b*x + c = 0
    
    Args:
        a (float): non-zero coefficient of x**2
        b (float): coefficient of x
        c (float): constant
    """

    def __init__(self, a, b, c):
        """
        Funcition run to initiate the class
        
        The input `self` is required for functions that belong to an object,
        meaning that you want to make the function access and/or depend on the 
        attributes of the object (e.g., self.time, and self.velocity below)
        """

       # let's initalize it's parent class (empty for now because it is a blank class)
        super().__init__()

        # Check if input is ok
        assert float(a)
        assert float(b)
        assert float(c)

        # Check if the equation is really quadratic
        if a == 0:
            print("This is not a quadratic equation")


        self.a = a
        self.b = b
        self.c = c

        
    def discriminant(self):
        """
        Computes the discriminant b**2 - 4*a*c of a quadratic equation
        """

        delta = (self.b**2) - (4*self.a*self.c)
        self.delta = delta
        '''
        if (delta < 0.0+0.0j):
            print("The quadratic equation has complex root(s)")
        elif (delta == 0.0+0.0j):
            print("The quadratic equation has real root and they are the same")
        else:
            print("The quadratic equation has two real roots")
        '''

    def find_x(self):
        """
        Solves the quadratic equation

        Returns:
            x1 (float): first solution (-b-sqrt(delta))/(2a)
            x2 (float): second solution (-b+sqrt(delta))/(2a)
        """
        self.discriminant()

        x1 = (-self.b-emath.sqrt(self.delta))/(2*self.a)  
        x2 = (-self.b+emath.sqrt(self.delta))/(2*self.a)

        self.x1 = x1
        self.x2 = x2

        print("The solutions are {:.2f} and {:.2f}". format(x1, x2))
        return x1, x2

    def image(self,x):
        """
        Computes the quadratic equation for a given x
        Args:
            x (float): number or array to compute
        """
        return self.a*x*x + self.b*x + self.c
    
    def plot(self):
        """
        Plot the quadratic equation in the xy real plane
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        self.find_x()
        ax.plot(linspace(-3+self.x1.real,self.x1.real+3), self.image(linspace(-3+self.x1.real,self.x1.real+3)), 0, label="$a = {}$\n$b = {}$\n$c = {}$".format(self.a,self.b,self.c) )

        
        ax.scatter(self.x1.real,0,self.x1.imag,label=r"$x_1$")
        ax.scatter(self.x2.real,0,self.x2.imag,label=r"$x_2$")

        
        # Set axis labels
        ax.set_xlabel(r'$x$ (Re)')
        ax.set_ylabel(r'$y$ (Re)')
        ax.set_zlabel(r'$z$ (Im)')

        ax.xaxis._axinfo["grid"]['linewidth'] = .3
        ax.yaxis._axinfo["grid"]['linewidth'] = .3
        ax.zaxis._axinfo["grid"]['linewidth'] = .3

        ax.view_init(110,270)
        fig.tight_layout()
        fig.subplots_adjust(right=0.8)
        ax.legend(loc='center left', bbox_to_anchor=(1.07, 0.5))
        plt.show()


y = QuadraticEquation(1,2,3)

y.find_x()
print(y.x1, y.x2)
#print(y.image(2))
y.plot()
