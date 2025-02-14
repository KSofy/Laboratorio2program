using System;

public class Variables
{
    public static void Main(string[] args)
    {
        // Declaración de variables
        int numeroEntero = 0;
        double numeroDecimal = 0;
        string texto = "";
        bool valorBooleano = false;


        Console.WriteLine("Cuál es tu edad:");
        string inputEntero = Console.ReadLine();

        while (!int.TryParse(inputEntero, out numeroEntero))
        {
            Console.WriteLine("Entrada no válida. Debes introducir un número entero:");
            inputEntero = Console.ReadLine();
        }

        Console.WriteLine("Introduce tu altura:");
        string inputDecimal = Console.ReadLine();

        while (!double.TryParse(inputDecimal, out numeroDecimal))
        {
            Console.WriteLine("Entrada no válida. Debes introducir un número decimal:");
            inputDecimal = Console.ReadLine();
        }

        Console.WriteLine("Introduce tu nombre:");
        texto = Console.ReadLine();

      
        Console.WriteLine("¿Tu informacion es verdadera? (true o false):");
        string inputBooleano = Console.ReadLine();

        while (!bool.TryParse(inputBooleano, out valorBooleano))
        {
            Console.WriteLine("Entrada no válida. Debes introducir 'true' o 'false':");
            inputBooleano = Console.ReadLine();
        }

        
        Console.WriteLine("\nEdad: " + numeroEntero);
        Console.WriteLine("Altura: " + numeroDecimal);
        Console.WriteLine("Nombre: " + texto);
        Console.WriteLine("Informacion: " + valorBooleano);
    }
}