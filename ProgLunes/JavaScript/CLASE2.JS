//creaion de array o arreglos
//Let autos = new array('ferrari','renault','bmw'); esta es la sintaxis vieja
const autos = ['ferrari','renault','bmw'];
console.log(autos);['ferrari','renault','bmw']

//recorremos los elementos de un arreglo
console.log(autos[0]);
console.log(autos[2]);

for(let i = 0; i < autos.length; i++){
    console.log(i+: |'+autos[i]);
}

//modificamos los elementos al arreglo
autos[1] = 'Volvio';
console.log(autos[1]);

//agregamos nuevos valores al arreglo
autos.push('Audi'); //agregamos el elemento al final del arreglo
console.log(autos); 

//otras formas de agregar elementos al arreglo
autos[autos.length] = 'porche'
console.log(autos);

//terera forma de agregar elementos teniendo CUIDADO
autos[6] ='renault';
console.log(autos);

//como preguntar si es una array o arreglo
console.log(Array.isarray(autos)); //devuelve un booleano


console.log(autos instanceof Array); //preguntamos si la variable es una instancia de la clase array


