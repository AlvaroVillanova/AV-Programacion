import java.util.Scanner;

//---------------ESTO ES UNA CLASE QUE SERA UTILIZADO POR EL MAIN.JAVA



/**
 * @author Alvaro Villanova
 * @version 0.01
 * 
 */

public class Circulo {

//-------------------------PRIMERO ATRIBUTO-----------

    // Atributos de circulo. ATRIBUTOS DEL PUBLIC CLASS CIRCULO
    private int radio;
    private String color;

    // Métodos de la clase

//-------------------------SEGUNDO CONSTRUCTORES -------

    /** Constructor por defecto.
     * 
     * Crea un circulo blanco con radio 1
     * 
     */
    public Circulo(){
        this.radio = 1;
        this.color = "blanco";
    }


    /** Constructor con parametros. 
     * 
     * Crea un circulo con un radio y color especificados.
     * 
     * @param radio El radio del circulo.
     * @param color El color del circulo.
     * @see Circulo#setRadio(int radio)
     */


    public Circulo(int radio, String color){
        // this.radio = radio;
        // if (radio <= 0) this.radio = 1; 
        this.setRadio(radio);
        this.color = color;
    }

    /** Constructor de copia.
     * Crea un circulo con un radio y color obtenido a partir de otro circulo.
     * @param c El circulo a copiar.
     */
    public Circulo(Circulo c){
        this.radio = c.radio;
        this.color = c.color;
    }

//---------------- TERCERO  GETS y SETS ------------------------

    /** Get -> Conseguir la información de los atributos.
     * Obtener el radio actual circulo
     * @return El radio del circulo
     */


    
    public int getRadio(){
        return this.radio;
    }

    /**
     * Obtener el color del circulo
     * @return El color del circulo
     */

    public String getColor(){
        return this.color;
    }

    // Set -> Establecer la información a los atributos.

    /**
     * Establece el radio del circulo
     * En caso de que el radio sea menor que cero (0), lo establece a 1.
     * @param radio El nuevo radio del circulo
     * @code if (luque) then luque
     * 
     */
    public void setRadio(int radio){
        this.radio = radio;
        if (radio <= 0) this.radio = 1; 
    }
    public void setColor(String color){
        this.color = color;
    }

    /**
     * Calcular el area del circulo. (AREA=pi*radio(al cuadrado))
     * @return area El area del circulo 
     */
    public double calcularArea(){ //Sera double porque casi seguro que es decimal al llevar PI  
        double area;
        area= Math.PI*this.radio*this.radio; // == Math.PI*Math.pow(this.radio,2)
        return area;
    } 

    /**
     * Calcular el perimetro del circulo    (PERIMETRO= 2*PI*Radio)
     * @return perimetro El perimetro del circulo
     */
    public double calcularPerimetro(){
        double perimetro;
        perimetro= 2*Math.PI*radio;
        return perimetro;
    }

    // Siempre se tiene que llamar así porque Java asume que cuando queremos 
    // mostrar por pantalla un circulo (print) tiene que llamar a toString().

    /**
     *  Devuelve en formato de cadena (String) del objeto Circulo
     * @return Una cadena que representa el objeto Circulo.
     */

    public String toString(){
        return "El radio es " + this.radio + " y el color es " + this.color + ".";
    }

    public static void main(String[] args) {
        // Scanner sc = new Scanner(System.in);

        // Constructor por defecto.
        Circulo circulitoPorDefecto = new Circulo();
        // Constructor por parámetros.
        Circulo circulitoConParametros = new Circulo(2,"azul");
        // Constructor de copia.
        Circulo circulitoDeCopia = new Circulo(circulitoConParametros);

        // System.out.println(circulitoPorDefecto.toString());

        System.out.println(circulitoPorDefecto);
        System.out.println(circulitoConParametros);
        System.out.println(circulitoDeCopia);

        circulitoDeCopia.setColor("rojo");
        circulitoDeCopia.setRadio(5);

        System.out.println(circulitoDeCopia);
        System.out.print("¿El circuloPorDefecto tiene el mismo radio que el circuloDeCopia? ");
        System.out.println(circulitoPorDefecto.getRadio() == circulitoDeCopia.getRadio());
        

        System.out.println("El area de circulitoDeCopia "+circulitoDeCopia+" es "+ circulitoDeCopia.calcularArea());
    }
}