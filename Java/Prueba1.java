import java.util.Scanner;

public class Prueba1{

    public static void main(String[] args){



        if(args.length == 1){

            if (args[0].equals("dia")){
                System.out.println("El dia es MARTES");
            }else if(args[0].equals("mes")){
                System.out.println("El mes es Enero! ");
            }else{
                System.out.println("MAAALLL!!! El argumento ha de ser mes o dia!");
            }

        }else{
            System.out.println("Esto esta mal");

        }
    }
}