import java.util.Scanner;

public class PT2{
    public static void main(String[] args){
        
        Scanner sc = new Scanner(System.in);

        int piezasAzulesCaja =      10;
        int piezasAmarillasCaja =   10;
        int piezasRojasCaja=        10;
        int piezasVerdesCaja=       10;

        int contadasAzules= 0;
        int contadasAmarillas= 0;
        int contadasRojas= 0;
        int contadasVerdes= 0;

        Boolean amarillasCorrectas,azulesCorrectas,rojasCorrectas,verdesCorrectas;

        System.out.println("Bienvenido! ");


        if (args.length == 4){
            System.out.println("Oye, buenos argumentos, cabessa. ");

            contadasAzules = Integer.parseInt(args.nextLine());
            contadasAmarillas = Integer.parseInt(args.nextLine());
            contadasRojas = Integer.parseInt(args.nextLine());
            contadasVerdes = Integer.parseInt(args.nextLine());


            // Comprobacion Azules
            if (contadasAzules > piezasAzulesCaja){
                System.out.println("Te sobran piezas Azules! ");
            } else if (contadasAzules<piezasAzulesCaja){
                System.out.println("Te faltan piezas Azules! ");
            } else {
                azulesCorrectas = true ;
            }

            // Comprobacion Amarillas
            if (contadasAmarillas > piezasAmarillasCaja){
                System.out.println("Te sobran piezas Amarillas! ");
            } else if (contadasAmarillas<piezasAmarillasCaja){
                System.out.println("Te faltan piezas Amarillas! ");
            } else {
                amarillasCorrectas = true ;
            }

            // Comprobacion Verdes
            if (contadasVerdes > piezasVerdesCaja){
                System.out.println("Te sobran piezas Verdes! ");
            } else if (contadasVerdes<piezasVerdesCaja){
                System.out.println("Te faltan piezas Verdes! ");
            } else {
                verdesCorrectas = true ;
            }

            // Comprobacion Rojas
            if (contadasRojas > piezasRojasCaja){
                System.out.println("Te sobran piezas Rojas! ");
            } else if (contadasRojas<piezasRojasCaja){
                System.out.println("Te faltan piezas Rojas! ");
            } else {
                rojasCorrectas = true ;
            }


        }
        else{

            System.out.println("Introduce cuantas piezas de cada color tienes (Azules/Amarillas/Rojas/Verdes.): ");
            contadasAzules = sc.nextInt();
            contadasAmarillas = sc.nextInt();
            contadasRojas= sc.nextInt();
            contadasVerdes= sc.nextInt();

            if( contadasAzules<piezasAzulesCaja || // Si hemos contado menos que las de las que deberian haber.
                contadasAmarillas<piezasAmarillasCaja ||
                contadasRojas<piezasRojasCaja ||
                contadasVerdes<piezasVerdesCaja){
                
                System.out.println("Faltan piezas!!! ");
                

            }else if(contadasAzules>piezasAzulesCaja || // Si hemos contado MAS de las que deberian haber.
                contadasAmarillas>piezasAmarillasCaja ||
                contadasRojas>piezasRojasCaja ||
                contadasVerdes>piezasVerdesCaja){
                
                System.out.println("Sobran piezas!!! ");
            }else{

                System.out.println("Piezas correctas! ");
            }



        }
    }
}

