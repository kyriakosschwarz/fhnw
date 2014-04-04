import Jama.CholeskyDecomposition;
import Jama.EigenvalueDecomposition;
import Jama.LUDecomposition;
import Jama.Matrix;

public class HilfsFunktionen {
	
	public static double spektralradius(Matrix A) {
		EigenvalueDecomposition ed = new EigenvalueDecomposition(A);
		
		double[] ev = ed.getRealEigenvalues();
		
		double max = Math.abs(ev[0]);
		
		for(int i = 1; i<ev.length; i++){
		
			double curr = Math.abs(ev[i]);
			
			if(curr > max) max = curr;
		}
		
		return max;
	}
	
	// das optimale omega fuer SOR
	public static double omega(Matrix A) throws Exception {
		
		if(!HilfsFunktionen.isTridiagonal(A)) throw new Exception("is not tridiagonal!");
		
		Matrix L = HilfsFunktionen.getLowerMatrix(A);
		
		Matrix U = HilfsFunktionen.getUpperMatrix(A);

		Matrix D = HilfsFunktionen.getDiagonalMatrix(A);
				
		Matrix AA = (D.minus(L)).inverse().times(U);
				
		double max = HilfsFunktionen.spektralradius(AA);
		
		double omega = 2/(1+Math.sqrt(1-max));
		
		return omega;
	}
	
	// NOT(!) LU Decompostion-- used for optimal omega calculation
	public static Matrix getDiagonalMatrix(Matrix A) {
		int size = A.getColumnDimension();
		
		double[][] d =new double[size][size];
		
		for(int i = 0; i<size; i++){
			d[i][i] = A.get(i, i);
		}
		
		Matrix D  = new Matrix(d);
		
		return D;
	}
	
	
	// NOT(!) LU Decompostion -- used for optimal omega calculation
	public static Matrix getLowerMatrix(Matrix A) {
		int size = A.getColumnDimension();
		
		double[][] l = new double[size][size];
		
		for(int i = 0; i<size; i++){
			for(int j=0; j < size; j++){
				if(j<i) l[i][j] = A.get(i, j);
			}
		}
		
		Matrix L = new Matrix(l);
	
		return L;
	}
	
	// NOT(!) LU Decompostion -- used for optimal omega calculation
	public static Matrix getUpperMatrix(Matrix A) {
		int size = A.getColumnDimension();
		
		double[][] u = new double[size][size];
		
		for(int i = 0; i<size; i++){
			for(int j=0; j < size; j++){
				if(j>i) u[i][j] = A.get(i, j);
			}
		}
		
		Matrix U = new Matrix(u);
		
		return U;
	}
	
	public static Matrix cholesky(Matrix A) throws Exception {
		CholeskyDecomposition cda = A.chol();
		
		if(!cda.isSPD()) {
			throw new Exception("Is NOT positive definite!");
		} else {
			Matrix L = cda.getL();
			return L;
		}		
	}
	
	// every COLUMN is an eigenvector
	public static Matrix eigenvectors(Matrix A) {
		EigenvalueDecomposition eda = A.eig();
		
		Matrix E = eda.getV();
		
		return E;
	}
	
	public static double[] eigenvalues(Matrix A) {
		EigenvalueDecomposition eda = A.eig();
		
		double[] e = eda.getRealEigenvalues();
		
		return e;
	}
	
	public static Matrix solveGauss(Matrix A, Matrix B) {
		Matrix S = A.solve(B);
		
		return S;
	}
	
	// LU Decomposition
	public static Matrix getL(Matrix A) {
		LUDecomposition lua = A.lu();
		
		Matrix L = lua.getL();
		
		return L;
	}
	
	// LU Decomposition
	public static Matrix getU(Matrix A) {
		LUDecomposition lua = A.lu();
		
		Matrix U = lua.getU();
		
		return U;
	}
	
	// LDL Decomposition
	public static Matrix getLL(Matrix AA){
		int n = AA.getColumnDimension();
		
		double[][] L = new double[n][n];
	    double[][] D = new double[n][n];
	    
	    double sum;
	    
	    double[][] A = new double[n][n];
	    
	    for(int i = 0; i<n; i++){
	    	for(int j =0; j<n; j++){
	    		A[i][j] = AA.get(i, j);
	    	}
	    }
	    	
	    D[0][0] = A[0][0];
	    L[0][0] = 1.0;
	    for (int j = 2; j <= n; j++) {
	      L[j-1][0] = A[j-1][0] / D[0][0];
	      L[j-1][j-1] = 1.0;
	    }
	    for (int i = 2; i <= n - 1; i++) {
	      sum = 0;
	      for (int k = 1; k <= i - 1; k++) sum += L[i-1][k-1] * L[i-1][k-1] * D[k-1][k-1];
	      D[i-1][i-1] = A[i-1][i-1] - sum;
	      for (int j = i + 1; j <= n; j++) {
	        sum = 0;
	        for (int k = 1; k <= i - 1; k++) sum += L[j-1][k-1] * L[i-1][k-1] * D[k-1][k-1];
	        L[j-1][i-1] = 1.0 / D[i-1][i-1] * (A[j-1][i-1] - sum);
	      }
	    }
	    sum=0;
	    for (int k=1; k<=n-1; k++)  sum += L[n-1][k-1] * L[n-1][k-1] * D[k-1][k-1];
	    D[n-1][n-1]= A[n-1][n-1]-sum;

	    Matrix LL = new Matrix(L);
	    
	    return LL;
	}
	
	// LDL Decomposition
	public static Matrix getDD(Matrix AA){
		int n = AA.getColumnDimension();
		
		double[][] L = new double[n][n];
	    double[][] D = new double[n][n];
	    
	    double sum;
	    
	    double[][] A = new double[n][n];
	    
	    for(int i = 0; i<n; i++){
	    	for(int j =0; j<n; j++){
	    		A[i][j] = AA.get(i, j);
	    	}
	    }
	    	
	    D[0][0] = A[0][0];
	    L[0][0] = 1.0;
	    for (int j = 2; j <= n; j++) {
	      L[j-1][0] = A[j-1][0] / D[0][0];
	      L[j-1][j-1] = 1.0;
	    }
	    for (int i = 2; i <= n - 1; i++) {
	      sum = 0;
	      for (int k = 1; k <= i - 1; k++) sum += L[i-1][k-1] * L[i-1][k-1] * D[k-1][k-1];
	      D[i-1][i-1] = A[i-1][i-1] - sum;
	      for (int j = i + 1; j <= n; j++) {
	        sum = 0;
	        for (int k = 1; k <= i - 1; k++) sum += L[j-1][k-1] * L[i-1][k-1] * D[k-1][k-1];
	        L[j-1][i-1] = 1.0 / D[i-1][i-1] * (A[j-1][i-1] - sum);
	      }
	    }
	    sum=0;
	    for (int k=1; k<=n-1; k++)  sum += L[n-1][k-1] * L[n-1][k-1] * D[k-1][k-1];
	    D[n-1][n-1]= A[n-1][n-1]-sum;

	    Matrix DD = new Matrix(D);
	    
	    return DD;
	}
	
	// LDL Decomposition
	public static Matrix getLT(Matrix AA) {
		Matrix LT = HilfsFunktionen.getLL(AA).transpose();
		return LT;
	}
	
	public static boolean isSymmetric(Matrix A) {
		int n = A.getColumnDimension();

		boolean is = true;
		for(int i = 0; i<n; i++){
	    	for(int j =0; j<n; j++){
	    		if(A.get(i, j) != A.get(j, i)) is = false;
	    	}
		}
		
		return is;
	}
	
	
	
	// Example: generateBigDiagonal(5, true, -1, 3, 2) // normal direction
	//    3     2     0     0     0
	//   -1     3     2     0     0
	//    0    -1     3     2     0
	//    0     0    -1     3     2
	//    0     0     0    -1     3
	
	// Example: generateBigDiagonal(5, true, -1, 3, 2) // opposite direction
	//    0     0     0    -1     3
    //	  0     0    -1     3     2
    //	  0    -1     3     2     0
	//   -1     3     2     0     0
    //    3     2     0     0     0
		
	// Accepts only 1,3 or 5 number of arguments (size and normal not included)
	public static Matrix generateBigDiagonal(int size, boolean oppositedirection, double... ds) throws Exception {
		double[][] a = new double[size][size];
		int numparams = ds.length;
		
		if(!oppositedirection) {
			switch(numparams) {
				case 1: for(int i = 0; i<size; i++){
			    			for(int j =0; j<size; j++){
			    				if(j == i) a[i][j] = ds[0];
			    			}
						}
						break;
				
				case 3: for(int i = 0; i<size; i++){
			    			for(int j =0; j<size; j++){
			    				if(j == i-1) a[i][j] = ds[0];
			    				if(j == i) a[i][j] = ds[1];
			    				if(j == i+1) a[i][j] = ds[2];
			    			}
						}
						break;
				
				case 5: for(int i = 0; i<size; i++){
	    					for(int j =0; j<size; j++){
	    						if(j == i-2) a[i][j] = ds[0];
	    						if(j == i-1) a[i][j] = ds[1];
	    						if(j == i) a[i][j] = ds[2];
	    						if(j == i+1) a[i][j] = ds[3];
	    						if(j == i+2) a[i][j] = ds[4];
	    					}
						}
						break;
				
				default: throw new Exception("Invalid number of parameters");
			}
		} else {
			switch(numparams) {
			case 1: for(int i = 0; i<size; i++){
		    			for(int j =0; j<size; j++){
		    				if(j+i == size-1) a[i][j] = ds[0];
		    			}
					}
					break;
			
			case 3: for(int i = 0; i<size; i++){
		    			for(int j =0; j<size; j++){
		    				if(j+i == size-2) a[i][j] = ds[0];
		    				if(j+i == size-1) a[i][j] = ds[1];
		    				if(j+i == size) a[i][j] = ds[2];
		    			}
					}
					break;
			
			case 5: for(int i = 0; i<size; i++){
    					for(int j =0; j<size; j++){
    						if(j+i == size-3) a[i][j] = ds[0];
    						if(j+i == size-2) a[i][j] = ds[1];
    						if(j+i == size-1) a[i][j] = ds[2];
    						if(j+i == size) a[i][j] = ds[3];
    						if(j+i == size+1) a[i][j] = ds[4];
    					}
					}
					break;
			
			default: throw new Exception("Invalid number of parameters");
			}
		}
		
		Matrix A = new Matrix(a);
	
		return A;
	}
	
	public static void solveJakobi(double[][] A, double[]b, double[] xOld) {
		int maxCount = 25;
		double eps = 1.0e-6;
		int n = A.length;
		
	    double[][] T = new double [n][n];
	    double[] x   = new double [n];

	    for (int i = 0; i < n ; i++) {
	        for (int k = 0; k < n ; k++)  T[i][k] = (-1.0)*A[i][k]/A[i][i];
	        T[i][i]=0.0;
	        b[i]=b[i]/A[i][i];
	        xOld[i]=b[i];
	      }
	      
	      int count=0;
	      double maxi;
	      System.out.println();
	      do  {
	        count++;
	        maxi=0;
	        for (int i = 0; i < n ; i++) {
	          x[i] = b[i];
	          for (int k = 0; k < n ; k++) x[i] +=T[i][k]*xOld[k];
	        }
	        
	        for (int i = 0; i < n ; i++) {
	          maxi=Math.max(maxi, Math.abs(xOld[i]-x[i]) );
	          xOld[i]=x[i];
	        }

	        InOut.print(count, 6, 0);
	        System.out.print(" Iteration :");
	        printVector(xOld);
	      } while(count < maxCount &&  maxi > eps  );

	      System.out.println();
	      if(count >= maxCount)
	      System.out.println("        ******* Jacobi NOT converged *******");
	 }
	
	public static void solveGaussSeidel(double[][] A, double[]b, double[] xOld) {
		int maxCount = 25;
		double eps = 1.0e-6;
		int n = A.length;
		
	    double[][] T = new double [n][n];
	    double[] x   = new double [n];
	    
	    for (int i = 0; i < n ; i++) {
	        for (int k = 0; k < n ; k++)  T[i][k] = (-1.0)*A[i][k]/A[i][i];
	        T[i][i]=0.0;
	        b[i]=b[i]/A[i][i];
	        xOld[i]=b[i];
	      }
	      
	      int count=0;
	      double maxi;
	      System.out.println();
	      
	      do  {
	        count++;
	        maxi=0;
	        for (int i = 0; i < n ; i++) {
	          x[i]=b[i]; 
	          for (int k = 0; k < n ; k++) x[i] +=T[i][k]*x[k];
	        }
	        
	        for (int i = 0; i < n ; i++) {
	          maxi=Math.max(maxi, Math.abs(xOld[i]-x[i]) );
	          xOld[i]=x[i];
	        }
	        
	        InOut.print(count, 6, 0);
	        System.out.print(" Iteration :");
	        printVector(xOld);
	      } while(count < maxCount &&  maxi > eps  );

	      System.out.println();
	      if(count >= maxCount)
	      System.out.println("        ******* Gauss-Seidel NOT converged *******");
	    
	}
	
	public static void solveSOR(double[][] A, double[]b, double[] xOld, double omega) {
		int maxCount = 25;
		double eps = 1.0e-6;
		int n = A.length;
		
	    double[][] T = new double [n][n];
	    double[] x   = new double [n];
	    for (int i = 0; i < n ; i++) {
	        for (int k = 0; k < n ; k++)  T[i][k] = (-1.0)*A[i][k]/A[i][i];
	        T[i][i]=0.0;
	        b[i]=b[i]/A[i][i];
	        x[i]=b[i];
	      }
	      
	      int count=0;
	      double maxi,sum;
	      System.out.println();
	      //InOut.print("Enter Relaxation-Factor :  ") ;
	      //double omega = InOut.getDouble()           ;
	   

	      do  {
	        count++;
	        maxi=0;
	        for (int i = 0; i < n ; i++) {
	          sum=0.0; 
	          for (int k = 0; k < n ; k++) sum +=T[i][k]*x[k];
	          x[i]=(1.0-omega)*x[i] + omega*(b[i]+sum);     
	        }
	        
	        for (int i = 0; i < n ; i++) {
	          maxi=Math.max(maxi, Math.abs(xOld[i]-x[i]) );
	          xOld[i]=x[i];
	        }
	        
	        InOut.print(count, 6, 0);
	        System.out.print(" Iteration :");
	        printVector(xOld);
	      } while(count < maxCount &&  maxi > eps  );
	      
	      System.out.println();
	      if(count >= maxCount)
	      System.out.println("        ******* SOR NOT converged *******");
	  }
	
	    
	 private static void printVector(double[] vec) {
	      for (int i = 0; i < vec.length; i++) {
	        InOut.print(vec[i], 6, 7);
	        System.out.print("  ");
	      }
	      System.out.print("\n");
	 }
	 
	 public static double[] fillxOld(int size, double val) {
		 double[] a = new double[size];
		 
		 for(int i =0; i<size; i++) {
			 a[i] = val;
		 }
		 
		 return a;
	 }
	 
	 public static double normMatrixInf(Matrix A) {
		 int size = A.getColumnDimension();
		 double max = 0;
		 for(int i = 0; i< size; i++) {
			 double sum = 0;
			 for(int j = 0; j< size; j++) {
				 sum += Math.abs(A.get(i, j)); 
			 }
			 if (sum > max) max = sum;
		 }
		 return max;
	 }
	 
	 public static double normMatrixTwo(Matrix A) {
		 return Math.sqrt(HilfsFunktionen.spektralradius(A.transpose().times(A)));
	 }
	 
	 public static boolean isConvergent(Matrix A) {
		 return HilfsFunktionen.spektralradius(A) < 1;
	 }
	 
	 public static boolean isTridiagonal(Matrix A) {
		 boolean is = true;
		 int n = A.getColumnDimension();
		 for(int i = 0; i<n; i++){
			 for(int j =0; j<n; j++){
				 if(((j==i)||(j==i-1)||(j==i+1))&&(A.get(i, j)==0)) {
					 is = false;
					 System.out.println("i: "+i +"   , j: "+j +"   , val: " + A.get(i, j));
				 }
				 if(((j<=i-2)||(j>=i+2))&&(A.get(i, j)!=0)) {
					 is = false;
					 System.out.println("i: "+i +"   , j: "+j +"   , val: " + A.get(i, j));

				 }
			 }
		 }
		 return is;
	 }
}
