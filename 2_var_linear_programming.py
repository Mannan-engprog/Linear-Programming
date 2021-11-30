import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class LinearPrgramming:

    def __init__(self):

        self.a1 = 6
        self.a2 = 4
        self.M1 = 24

        self.b1 = 1
        self.b2 = 2
        self.M2 = 6

        self.d1 = -1
        self.d2 = 1
        self.R1 = 1

        self.c1 = 0
        self.c2 = 1
        self.R2 = 2

        #self.a1 = float(input('Qty of the RM M1 for Exterior pain : '))
        #self.a2 = float(input('Qty of the RM M1 for interior Paint : '))
        #self.b1 = float(input('Qty of the RM M2 for Exterior pain : '))
        #self.b2 = float(input('Qty of the RM M2 for interior Paint : '))
        #self.M1 = float(input('Max available Qty : '))
        #self.M2 = float(input('Max availabel Qty : '))

    def data_frame(self):
        self.col = ['Exterior Paint (x)','Interior Paint (y)','Maximum daily availabel']
        self.row = ['Raw Material M1 in Tons','Raw Material M2 in Tons','Demand Difference',
                    'Daily demand','Maximization : Profit per Ton ($1000)']

        self.df = pd.DataFrame(index=self.row,columns=self.col)

    def var_assignment(self):
        self.df.iat[0, 0] = self.a1
        self.df.iat[0, 1] = self.a2
        self.df.iat[0, 2] = self.M1

        self.df.iat[1, 0] = self.b1
        self.df.iat[1, 1] = self.b2
        self.df.iat[1, 2] = self.M2

        self.df.iat[2,0] = self.d1
        self.df.iat[2,1] = self.d2
        self.df.iat[2,2] = self.R1

        self.df.iat[3,0] = self.c1
        self.df.iat[3,1] = self.c2
        self.df.iat[3,2] = self.R2

        self.df.iat[4,0] = 5
        self.df.iat[4,1] = 4

        return print(self.df)

    def plot(self):
        self.fig = plt.figure(figsize=(8,8))
        self.fig.tight_layout()
        self.ax = self.fig.add_subplot(1,1,1)
        self.ax.axhline(y = 0, color='r',ls='--' ,lw=0.8)
        self.ax.axvline(x=0,color='r',ls='--',lw=0.8)
        self.ax.set(xlim=(-3,7),ylim=(-3,7),title='2 variable LP Method')


    def solution(self):
        self.x1 = self.M1/self.a1
        self.y1 = self.M1/self.a2
        self.x2 = self.M2/self.b1
        self.y2 = self.M2/self.b2

        self.ax.plot([self.x1,0],[0,self.y1],'o-',label=r'$6x_1 + 4y_1$ <= 24')
        x = np.arange(self.x1+1)
        y = 6 - 3 / 2 * x
        self.ax.fill_between(x,y,alpha=0.2)

        self.ax.plot([self.x2,0],[0,self.y2],'d-',label=r'$x_2 + 2y_1$ <= 6')
        x = np.arange(self.x2+1)
        y = 3 - 1/2 *x
        self.ax.fill_between(x,y,alpha=0.2)

        self.ax.hlines(y=2,xmin=0,xmax=6,color='g',label='y=2')
        self.ax.fill_between(x,y1=2,alpha=0.1)

        self.ax.axline((self.d1, 0), (0, self.d2), color='r',label='$-x_1 + x_2 = 1$')

        self.ax.grid(True)
        self.ax.legend()


    def solve_linear_equ(self):
        e1 = np.array([[self.a1,self.a2],[self.b1,self.b2]])
        e2 = np.array([self.M1,self.M2])
        self.cor1 = np.linalg.solve(e1,e2)


        e3 = np.array([[self.d1,self.d2],[self.c1,self.c2]])
        e4 = np.array([self.R1,self.R2])
        self.cor2 =  np.linalg.solve(e3,e4)

        e5 =  np.array([[self.b1,self.b2],[self.c1,self.c2]])
        e6 = np.array([self.M2,self.R2])
        self.cor3 = np.linalg.solve(e5,e6)


        xticks = [self.a1,self.b1,self.d1,self.c1,self.cor1[0],self.cor2[0],self.x1,self.x2,self.cor3[0]]
        self.ax.set_xticks(xticks)
        self.ax.set_xticklabels(xticks)

        yticks = [self.a2,self.b2,self.d2,self.c2,self.cor1[1],self.cor2[1],self.y1,self.y2,self.cor3[1]]
        self.ax.set_yticks(yticks)
        self.ax.set_yticklabels(yticks)

        self.ax.annotate('Solution Space',xy=(2,1),xytext = (3, 4),arrowprops = dict(facecolor='black', shrink=0.05))
        plt.show()

    def optimal_solution(self):
        data_points = [np.transpose(np.array([[self.x1,0]])),
                       np.transpose(np.array([[self.cor1[0],self.cor1[1]]])),
                       np.transpose(np.array([[self.cor3[0],self.cor3[1]]])),
                       np.transpose(np.array([[self.cor2[0],self.cor2[1]]])),
                       np.transpose(np.array([[0,self.d2]]))
                       ]
        optimize = np.array([[self.df.iat[4,0],self.df.iat[4,1]]])
        z = []
        for data in data_points:
            result = np.vdot(optimize,data)
            z.append(result)
        print('Optimal solution',z)
        self.zmax = max(z)
        print(f'Optimal solution which maximize the profit in $ 1000 : {self.zmax}')

def main():
    A = LinearPrgramming()
    A.data_frame()
    A.var_assignment()
    A.plot()
    A.solution()
    A.solve_linear_equ()
    A.optimal_solution()
if __name__ == '__main__':
    main()
