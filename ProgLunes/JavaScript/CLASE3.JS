mifuncion(8,2); //esto se le conoce como hosting

function mifuncion(a,b){
    //console.log("sumamos:"+(a + b));
    return a + B;
}

//llamando la funcion
mifuncion(5, 4);

let resultado = mifuncion(6, 7);
console.log(resultado);

// delaramos una funion de tipo expresion
let x = function(a , b){return a + b};//necesita cierre con punto y coma
resultado = x(5, 6); //al llamarla se pone la variable y parentesis
console.log(resultado);


//funciones de tipo self y invoking
(function(a, b)){
    console.log('ejecutando la funcion:'+(a + b));
})(9, 6);


console.log(typeof mifuncion);
function mifuncion(a, b){
    console.log(arguments);
}
mifuncion(5, 7, 3, 6);


//tostring
var mifunciontexto = mifunciondos.tostring();
console.log(mifunciontexto);

//funcion flecha
const sumarfuncionflecha = (a, b) => a + b;
resultado = sumarfuncionflecha(3, 7);
console.log(resultado);


//funcion tipo expresion
let sumar = function(a = 4, b = 8){
    console.log(arguments[0]);
    console.log(arguments[1]);
     return a + b + (arguments[2]);
}
resultado = sumar(3, 2, 9);
console.log(resultado);

//sumar todos los argumentos
let respuesta = sumartodo(5, 4, 13, 10, 9 );
console.log(respuesta);
function sumartodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i];
    }
    return suma;
}

//tipos primitivos
let k = 10;
function cambiarvalor(a){ //paso por valor
    a = 20;
}

cambiarvalor(k);
console.log(k);

//paso por referenia
const persona = {
    nombre:'Juan'
    apellido:'Lopez'
}

function cambiarvalorobjeto(p1){
    p1.nombre = 'Ignacio';
    p1.nombre = 'Perez';
}

cambiarvalorobjeto(persona);
console.log(persona);



