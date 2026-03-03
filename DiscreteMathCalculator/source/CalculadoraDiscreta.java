package discreteMath;
import java.util.Scanner;
import discreteMath.Discrete.*;

public class CalculadoraDiscreta
{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		boolean calculando = true;
		int m = 0;
		int n = 0;
		int len = 0;
		String opcion = "";
		// MENU
		while(calculando) {
			System.out.println("==========================================");
			System.out.println("ELIJA UNA OPCIÓN:");
			System.out.println("1. Permutación");
			System.out.println("2. Permutación con repetición restringida");
			System.out.println("3. Permutación circular");
			System.out.println("4. Variación ordinaria");
			System.out.println("5. Variación con repetición");
			System.out.println("6. Variación circular");
			System.out.println("7. Combinación");
			System.out.println("8. Combinación circular");
			System.out.println("9. Combinaciones con repetición");
			System.out.println("0. Salir");
			opcion = sc.nextLine();
			
			
			// OPCIONES
			
			
			// Permutación - ord
			if(opcion.equals("1")) {
				System.out.println("Introduce los argumentos:");
				m = sc.nextInt();
				System.out.println("RESULTADO:");
				System.out.println(Discrete.factorial(m)); 
			}
			
			
			// Permutación - repetición restringida
			else if(opcion.equals("2")) {
				System.out.println("Introduce la cantidad de argumentos:");
				len = sc.nextInt();
				System.out.println("Introduce los argumentos:");
				int numeros[] = new int[len];
				for(int i=0; i<len; i++) {
					numeros[i] = sc.nextInt();
				}
				System.out.println("RESULTADO:");
				System.out.println(Discrete.perr(numeros)); 
			}
			
			
			// Permutación - circular
			else if(opcion.equals("3")) {
				System.out.println("Introduce los argumentos:");
				m = sc.nextInt();
				System.out.println("RESULTADO:");
				System.out.println(Discrete.perc(m)); 
			}
			
			
			// Variación - ord
			else if(opcion.equals("4")) {
				System.out.println("Introduce los argumentos:");
				m = sc.nextInt();
				n = sc.nextInt();
				System.out.println("RESULTADO:");
				System.out.println(Discrete.var(m,n));
			}
			
			
			// Variación - repetición
			else if(opcion.equals("5")) {
				System.out.println("Introduce los argumentos:");
				m = sc.nextInt();
				n = sc.nextInt();
				System.out.println("RESULTADO:");
				System.out.println(Discrete.varr(m,n));
			}
			
			
			// Variación - circular
			else if(opcion.equals("6")) {
				System.out.println("Introduce los argumentos:");
				m = sc.nextInt();
				n = sc.nextInt();
				System.out.println("RESULTADO:");
				System.out.println(Discrete.varc(m,n));
			}
			
			
			// Combinación - ord
			else if(opcion.equals("7")) {
				System.out.println("Introduce los argumentos:");
				m = sc.nextInt();
				n = sc.nextInt();
				System.out.println("RESULTADO:");
				System.out.println(Discrete.comb(m,n));
			}
			
			
			// Combinación - circular
			else if(opcion.equals("8")) {
				System.out.println("Introduce los argumentos:");
				m = sc.nextInt();
				n = sc.nextInt();
				System.out.println("RESULTADO:");
				System.out.println(Discrete.combc(m,n));
			}
			
			
			// Combinacion - repetición
			else if(opcion.equals("9")) {
				System.out.println("Introduce los argumentos:");
				m = sc.nextInt();
				n = sc.nextInt();
				System.out.println("RESULTADO:");
				System.out.println(Discrete.combr(m,n));
			}
			
			
			// Exit
			else if(opcion.equals("0")) {calculando = false;}
			else{System.out.println("La opción elegida no está disponible.");}
			if(calculando) {sc.nextLine();}
		}
	}
}
