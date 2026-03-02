package discreteMath;

/**
 * Utilidades esenciales para cálculos matemáticos discretos
 * @author Eneko
 * @version 1.0
 */
public class Discrete
{	
	public static void main(String[] args){
		//System.out.println(factorial(1));
		//System.out.println(comb(2,1));
		//System.out.println(var());
		//System.out.println(varr());
		//System.out.println(varc(5,4));
		//System.out.println(perc());
		//System.out.println(perr(3,3,3));
		//System.out.println(combr());
	}
	/**
	 * Cálcula todas las formas posibles de ordenar un conjunto m de elementos
	 * @param int x>=0
	 * @return (x)*(x-1)*(x-2)*...*(1)
	 */
	public static long factorial(int x)
	{
		if(x<0) {x = 0;}
		if(x==0) {return 1;}
		long resultado = x;
		for(int i=x-1; i>0; i--) {
			resultado = (long) resultado*i;
		}
		return (long) resultado;
	}
	/**
	 * Cálcula los diferentes grupos de n elementos que se pueden 
	 * obtener de un montón m (m>=n)
	 * @param m>=1
	 * @param n>=1
	 * @return long x
	 */
	public static long comb(int m, int n)
	{
		if(m<1 || n<1) {System.err.println("m y n deben de ser mayores que 0."); return 1;}
		if(n>m) {System.err.println("m debe de ser mayor o igual a n"); return 1;}
		int denominador = m-n; 
		int maximo = (denominador>n) ? denominador : n;
		long divisor = 1;
		if(m-1 >= maximo) {divisor = m;}
		for(int i=m-1; i>maximo; i--) {
			divisor *= i;
		} 
		long resultado = (maximo == denominador) ? (divisor/factorial(n)) : (divisor/factorial(m-n));
		return (long) resultado;
	}
	
	
	/**
	 * Cálcula los diferentes grupos de n elementos que se pueden 
	 * obtener de un montón m en un contexto circular
	 * @param m>=1
	 * @param n>=1
	 * @return long x
	 */
	public static long combc(int m, int n)
	{
		if(m<1 | n<1) {System.err.println("m y n deben de ser mayores que 0."); return 1;}
		int arriba = m+n-1;
		int maximo = (n>m-1) ? n : m-1;
		for(int i=m+n-2; i>maximo; i--) {
			arriba *= i;
		}
		if(maximo == n) {return arriba/factorial(m-1);}
		else {return arriba/factorial(n);}
	}
	
	
	/**
	 * Cálcula todas las maneras en las que se podrían ordenar todos los 
	 * diferentes grupos de n elementos que se pueden optener de un montón m (m>=n)
	 * @param m>=1
	 * @param n>=1
	 * @return long x
	 */
	public static long var(int m, int n)
	{
		if(m<1 | n<1) {System.err.println("m y n deben de ser mayores que 0."); return 1;}
		if(n>m) {System.err.println("m debe de ser mayor o igual a n"); return 1;}
		int denominador = m-n;
		long resultado = m;
		for(int i=m-1; i>denominador; i--) {
			resultado *= i;
		} return (long) resultado;
	}
	/**
	 * Calcula todas las formas posibles de seleccionar y ordenar un 
	 * grupo de n elementos a partir de un conjunto total 
	 * de m elementos (los elementos pueden repetirse)
	 * @param m conjunto total de elementos a ordenar
	 * @param n tamaño de los grupos a seleccionar y ordenar
	 * @return m^n
	 */
	public static long varr(int m, int n)
	{
		long resultado = m;
		for(int i=1; i<n; i++) {
			resultado *= m;
		} return (long) resultado;
	}
	
	/**
	 * Calcula todas las formas posibles de seleccionar y ordenar un grupo 
	 * de elementos a partir de un total de elementos en un contexto circular 
	 * (no existe un primer ni un último lugar) n<m
	 * @param m conjunto total de elementos a ordenar (m>0)
	 * @param n tamaño de los grupos a seleccionar y ordenar (n>0)
	 * @return long x
	 */
	public static long varc(int m, int n)
	{
		if(m<1 || n<1) {System.err.println("m y n deben de ser mayores que 0."); return 1;}
		if(n>m) {System.err.println("m debe de ser mayor o igual a n"); return 1;}
		int denominador = m-n;
		long resultado = m;
		for(int i=m-1; i>denominador; i--) {
			resultado *= i;
		} return (long) resultado/n;
	}
	
	/**
	 * Calcula todas las formas posibles de ordenar un 
	 * grupo de n elementos a partir de un conjunto total 
	 * de m elementos (los elementos tienen una repetición limitada por restricciones)
	 * @param numeros x1, x2, x3, x4, ..., xn (x>0)
	 * @return long x
	 */
	public static long perr(int... numeros)
	{
		boolean buscando = true;
		int divisor = 1;
		int maximo = 0;
		int temp = 0;
		long denominador = 1;
		for(int n : numeros) {
			if(n<0) {System.err.println("El argumento x no puede ser menor que 0"); return 1;}
			temp += n;
			if(n>maximo) {maximo = n;}
		} 	
		if(temp-1 >= maximo) {divisor = temp;}
		for(int i=divisor-1; i>maximo; i--) {
			divisor *= i;
		} 
		for(int n : numeros) {
			if(n==maximo && buscando) {buscando = false;} 
			else {denominador *= factorial(n);}
		}
		return (long) divisor/denominador;
	}
	
	
	/**
	 * Cálcula todas las formas posibles de ordenar un del entero 
	 * introducido conjunto m de elementos en un contexto circular
	 * @param int x>=0
	 * @return (x-1)*(x-2)*(x-3)...*(1)
	 */
	public static long perc(int m)
	{
		if(m<0) {System.err.println("El metodo factorial no admite argumentos negativos."); return 1;}
		if(m==0) {return 1;}
		return factorial(m-1);
	}
	
	/**
	 * Cálcula los diferentes grupos de n elementos que se pueden 
	 * obtener de un montón m con repeticiones (m>=n)
	 * @param m>=1
	 * @param n>0
	 * @return long x
	 */
	public static long combr(int m, int n)
	{
		if(m<1) {System.err.println("m debe de ser mayor que 0."); return 1;}
		if(n<0) {System.err.println("n debe de ser mayor o igual a 0."); return 1;}
		if(n == 0) {return 1;}
		int denominador = m-1; 
		int maximo = (denominador>n) ? denominador : n;
		long divisor = 1;
		if(m+n-2 >= maximo) {divisor = m+n-1;}
		for(int i=m+n-2; i>maximo; i--) {
			divisor *= i;
		} 
		long resultado = (maximo == denominador) ? (divisor/factorial(n)) : (divisor/factorial(m-1));
		return (long) resultado;
	}
}