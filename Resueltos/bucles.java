public class bucles{
    public static void main (String[] args){

        // FOR EACH  -> for num in listaNum :

        String[] listaAzules = {"Azul","Anil","Indigo","Cobalto","Klein"};
        for (String azul : listaAzules){
            System.out.println(azul);
        }

        // FOR --> No existe en Python

        for (int contador=0; contador<10; contador++){
            System.out.println(contador);
        }

        // WHILE -> 

        System.out.print("BUCLE WHILE!!! ")
        
        while (!salir){
            System.out.println("Escribe salir: ");
            palabra = sc.nextLine();
            if (palabra.equals("salir")){
                salir= true;
            }


        }


    }
}