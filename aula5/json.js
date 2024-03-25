// {
//     $jsonSchema: {
//       bsonType: 'object',
//       required: [
//         '_id',
//         'titulo',
//         'autor',
//         'ano',
//         'preco'
//       ],
//       properties: {
//         _id: {
//           bsonType: 'objectId',
//           description: 'ID do livro'
//         },
//         titulo: {
//           bsonType: 'string',
//           description: 'deve ser uma string'
//         },
//         autor: {
//           bsonType: 'string',
//           description: 'deve ser uma string'
//         },
//         ano: {
//           bsonType: 'int',
//           description: 'deve ser um inteiro'
//         },
//         preco: {
//           bsonType: 'double',
//           description: 'deve ser um número de ponto flutuante'
//         }
//       }
//     }
//   }