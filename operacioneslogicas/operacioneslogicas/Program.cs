
Console.WriteLine("Ingresa el primer número: ");
int num1 =
    int.Parse(Console.ReadLine());

Console.WriteLine("Ingresa el segundo número: ");
int num2 =
    int.Parse(Console.ReadLine());


bool esMayor = num1 > num2;
bool esMenor = num1 < num2;
bool esIgual = num1 == num2;


bool algunoPositivo = num1 > 0 || num2 > 0;
bool algunoNegativo = num1 < 0 || num2 < 0;

Console.WriteLine($"\n¿{num1} es mayor que {num2}?: {esMayor}");

Console.WriteLine($"¿{num1} es menor que {num2}?: {esMenor}");

Console.WriteLine($"¿{num1} es igual a {num2}?: {esIgual}");

Console.WriteLine($"¿Alguno es positivo?: {algunoPositivo}");

Console.WriteLine($"¿Alguno es negativo?: {algunoNegativo}");
