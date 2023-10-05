function getInputFunction() {
    // Obtén la entrada del usuario
    var expresion = document.getElementById("logic-function").value;
    return expresion;
}
  
function makeFunction() {
    var f = getInputFunction();
  
    try {
        // Encuentra todas las letras (variables) en la expresión utilizando una expresión regular
        var variables = f.match(/[a-zA-Z]+/g);

        // Elimina las variables duplicadas
        variables = Array.from(new Set(variables));

        // Crea una función anónima que tome un objeto de valores como entrada y evalúe la expresión
        var dynamicFunction = new Function("values", `
          var ${variables.join(", ")}; // Declara las variables
          return (${f}); // Evalúa la expresión
        `);

        return dynamicFunction;
    } catch (error) {
        console.error('Error al evaluar la expresión:', error);
    }
}
  
// Ejemplo de uso:
var userFunction = makeFunction();

// Define los valores de las variables (por ejemplo, A y C)
var values = {
  A: true,
  C: false
};

// Evalúa la expresión con los valores proporcionados
var resultado = userFunction(values);

console.log(resultado); // El resultado de la expresión con los valores dados
  