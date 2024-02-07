public class Libro {  // (1) Creamos la clase -----------   Esta clase va a ser usada por nuestro Main.java     ;    Una clase es como una funcion.
    

    //
    //  1 - Primero creamos el nombre de la clase (public class Libro{}) que sera usado por Main.java
    //  2 - (Opcional) Se crea el main para testear que la clase funciona bien
    //  3 - Creamos los atributos (que son atributos generales usados por el resto de sub-clases)
    //  4 - Creamos el constructor (this.titulo hace que se le asigne un titulo a ESE NUEVO LIBRO, pero usando uno de los atributos generales. "this" tambien es util para saber que se esta usando un atributo general y no una variable cualquiera recien generada)
    //  5 - Creamos el get y el set (get sirve para leer info dentro de objetos, set para cambiar info de los objetos.)
    //  6 - Creamos el toString (Esto formateara el contenido de nuestro objeto para que pueda representarse al hacer un print.)
    //


    // (3)------- CREAMOS LOS ATRIBUTOS --------------------------------------------------------------------------------------------------------

    private String titulo;
    private String autor;
    private int numPaginas;
    private final int ISBN;  // final crea la variable como CONSTANTE; no se puede modificar despues de atribuirle un valor
    

    // (4)------- SEGUNDO CREAMOS EL CONSTRUCTOR -----------------------------------------------------------------------------------------------------


    // Podemos crear diferentes constructores para diferentes usos (como crear diferentes funciones).

    /**
     * Constructor con parametros TITULO y ISBN.
     * Crear un libro con un titulo y ISBN especificados.
     * @param titulo El titulo del libro.
     * @param ISBN El ISBN del libro
     */

    public Libro(String titulo, int ISBN){   // OJO CON LA SOBRECARGA DE ATRIBUTOS; solo puede escoger uno u otro si le alimentamos los mismos atributos.
        
        this.titulo = titulo;
        this.autor = "";
        this.ISBN = ISBN;
        this.numPaginas = 0;

    }

    /**
     * Constructor con TODOS los parametros.
     * Crear un libro con un titulo, autor, ISBN y num de paginas.
     * @param titulo El titulo del libro.
     * @param autor El autor del libro.
     * @param ISBN El ISBN del libro.
     * @param numPaginas El numero de paginas del libro.
     */


    public Libro(String titulo, String autor, int ISBN, int numPaginas){
        
        this.titulo = setTitulo(titulo);
        this.autor= autor;
        this.ISBN = ISBN;
        this.numPaginas = numPaginas;

    }
    // (5) ------------------------CREAMOS LOS GETS Y SETS----------------------------------------------------------------------------------
    //------------ GETS ------------
    /**
     * Obtener el titulo actual del libro
     * @return El titulo del titulo
     * 
     */
    public String getTitulo(){
        return this.titulo;
    }

     /**
     * Obtener el autor actual del libro
     * @return El autor del titulo
     * 
     */
    public String getAutor(){
        return this.autor;
    }
     /**
     * Obtener el ISBN actual del libro
     * @return El ISBN del titulo
     * 
     */
    public int getISBN(){
        return this.ISBN;
    }
         /**
     * Obtener el numPaginas actual del libro
     * @return El numPaginas del titulo
     * 
     */
    public int getnumPaginas(){
        return this.numPaginas;
    }
    //--------- SETS -------------
    /**
     * Establecer el titulo actual del libro
     * @param titulo El nuevo titulo del libro
     * 
     */
    public String setTitulo(String titulo){

        if (titulo.length()>20){
            String aux="";
            for (int i=0;i<20;i++){
                aux += titulo.charAt(i);   
            }
            titulo=aux;
        }
        this.titulo=titulo;
        return titulo;
    }

    /**
     * Establecer el autor actual del libro
     * @param autor El nuevo autor del libro
     * 
     */
    public void setAutor(String autor){

        if (autor.length()>20){

            String inicial="";
            String nombre="";
            int longitudPalabra;

            inicial+=autor.charAt(0);
            inicial+=" ";
            longitudPalabra=autor.length();

            for (int i=0; i<longitudPalabra;i++){
                if (autor.charAt(i)==' '){
                    inicial+=autor.charAt(i+1);
                    inicial+=".";
                }
            }
            inicial=inicial.toUpperCase();
            autor=inicial; 
        }
        this.autor = autor;
    }

    /**
     * Establecer el numPaginas actual del libro
     * @param numPaginas El nuevo numPaginas del libro
     * 
     */
    public void setNumPaginas(int numPaginas){

        if (numPaginas<0) numPaginas = 0;
        this.numPaginas = numPaginas;
    }



    /** ---(6)------------------------------------------ CREAMOS TO STRING ---------------------------------------------------------------------
     *  Devolver la representacion en formato de cadena (String) del objeto libro.
     *  
     */

    // Siempre se tiene que llamar así porque Java asume que cuando queremos 
    // mostrar por pantalla un circulo (print) tiene que llamar a toString().

    public String toString(){
        return "El libro"+this.titulo+", de "+this.autor+", con ISBN: "+this.ISBN+". Tiene "+this.numPaginas+" paginas. ";
    
    }


    public static void main(String[] args){    // --(2)---- Creamos el main (esto es opcional, se usa para comprobar que todo funciona bien)
        
            Libro libro2 = new Libro("Pepe Va al Metaverso Y Se Encuentra Con Muchos Colegas","William Shakespeare Manuel Manoles Cordura",123456789,-236);    ///------------> Este llamaria a nuestro segundo constructor (el de cuatro parametros)
            //System.out.println("El libro 2 es : "+libro2);
            System.out.println(libro2);
            
            String auxAlpha;
            int auxNum;

            auxAlpha="pedroooooooooooooooooooooooooooooooooooaaaaaaaaaaaaaaaaeeeeeeeeeeeeiiiiiiiiii";            
            libro2.setAutor(auxAlpha);

            auxAlpha="Cacacarotototo asdf wertewrt erytt qwerqrwewer tgfdsg dgfg zxc";
            libro2.setTitulo(auxAlpha);

            auxNum=-50;
            libro2.setNumPaginas(auxNum);

            System.out.println(libro2);
            
        }
}

//-------------------------------------------------------------------------------------------------------

// EJERS   ----- Esto se escribe dentro de los SETS y los CONSTRUCTORES.

// El numero de paginas introducidas no puede ser menor de 0.
// Si al crear el objeto se introduce un numero de paginas negativa, se cambia a 0.
// Si al cambiar el valor del numero de paginas, es negativa, se deja el que estaba.
//
// Tanto el titulo como el autor no pueden tener mas de 20 caracteres.
// En caso de tener mas,el titulo se trunca.
// En el autor se ponen las iniciales.