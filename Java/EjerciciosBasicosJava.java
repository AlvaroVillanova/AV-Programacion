import java.util.Scanner;


public class EjerciciosBasicosJava{
    public static void main(String[] args){

        String palabra,palabra2,colorGuardado,color;
        int numero1,numero2,numero3,repeticiones;

        Scanner sc = new Scanner(System.in);

        //Ej 0 Solicita por teclado un color. Guardalo para más tarde.

        System.out.println("0. Dime un color: ");
        colorGuardado=sc.nextLine();

        //Ej 1 Solicita por teclado una palabra e imprimela de nuevo.
        System.out.println("1. Dime una palabra: ");
        palabra = sc.nextLine();
        System.out.println(palabra);

        //Ej 2 Solicita por teclado una palabra y repítela 5 veces.

        repeticiones=5;

        System.out.println("2. Dime una palabra: ");
        palabra = sc.nextLine();
        System.out.println(palabra.repeat(" ",repeticiones));

        //Ej 3 Solicita por teclado una palabra y repítela 5 veces separándola por espacios.
        //Ej 4 Solicita una palabra y un número. Repite la palabra tantas veces como indique el número.
        //Ej 5 Solicita una palabra y un número. Muestra por pantalla: 'Tengo <numero> <palabra>s'.

        // ---------- OPERADORES --------------
        //Ej 6 Solicita por teclado un número y multiplícalo por 0.
        //Ej 7 Solicita por teclado dos números y multiplícalos entre sí.
        //Ej 8 Solicita por teclado dos números y escribe true si el primero es mayor.
        //Ej 9 Solicita por teclado un número y escribe true si es par.
        //EJ 9.1 Solicita por teclado un número y escribe true si es multiplo de 5.


        // ----------- CONDICIONALES -----------
        //Ej 10 Solicita por teclado dos numeros y la palabra 'suma' o 'resta'. Realiza la operación correspondiente.
        //Ej 11 Solicita por teclado dos numeros. Escribe 'El primer número es mayor' o 'El primer número es menor' segun corresponda.
        //Ej 12 Solicita por teclado dos numeros. Escribe 'Has ganado' si el segundo número menos el primero da un valor positivo.
        //Ej 13 Solicita por teclado un color. Si coincide con el color del ejercicio #0 escribe '¿Cómo sabías que era mi color favorito?
        //Ej 14 Solicita por teclado un día de la semana y un número. Si el número coincide con su día de la semana o el día introducido es viernes escribe ¡Has ganado!
        //Ej 15 Solicita por teclado tres números. Si los dos primeros son mayores que el tercero, escribe 'Mayores'; si los dos son menores que el tercero, escribe 'Menores'; para cualquier otro caso, escribe '¿Iguales?














    }
}