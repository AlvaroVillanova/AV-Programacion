import java.util.Scanner;

public class Condicionales{

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);


        Integer dato = Integer.parseInt(args[0]);

        System.out.println("Tu numero es... ");

        if (dato < 0){
            System.out.println("Numero negativo! ");
        } else if (dato > -1){
            System.out.println("Numero positivo! " + dato);
        } else{
            System.out.println("Esto no es un numero. + dato ");
        }
        
        System.out.println(palabra);






    }
}