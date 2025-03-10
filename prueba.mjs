#!/usr/bin/env zx

console.log(chalk.blue('Obteniendo información del sistema...'))
await sleep(1000)

console.log('Usuario:', os.userInfo().username)
console.log('Sistema operativo:', os.platform())

const name = await question('¿Cuál es tu nombre? ')
console.log(chalk.green(`¡Hola, ${name}!`))
