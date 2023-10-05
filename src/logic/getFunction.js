// A * B + C
// AB * C +

// (-(A * B) + C) * D
// (E1) * E2  = E1 E2 *
// E1 = (E1_1) + E1_2 = E1_1 E1_2 +
// E1_1 = E1_1_1 * E1_1_2 = E1_1_1 E1_1_2 *
// E1_1_1 E1_1_2* E1_2+ E2*

//A * B + C * D
// E1 + E2 = E1 E2 +
// E1 = -E1_1 * E1_2 = E1_1 - E1_2 *
// E2 = E2_1 * E2_2 = E2_1 E2_2 *
// E1_1 - E1_2 * E2_1 E2_2 * +

// (A + B * C) * (D + E) + F

// for (let index = 0; index < fx.length; index++) {
//     const character = fx[index];
//     if (operators.indexOf(character) !== -1) {
//         Operator operator = new Operator('character', index);
//         fxOperators.push(operator);
//     } elif (/^[A-Z]$/.test(character) || limiters.indexOf(character) !== -1) {
//         Element element = new Element(character, index, index);
//         fxElements.push(element);
//     }
// }

class Element {
    constructor(character, position) {
        this.character = character;
        this.position = position;
        this.element = null;
    }

    setElement(element) {
        this.element = element;
    }
}

class Operator {
    constructor(type, position) {
        this.type = type;
        this.position = position;
    }
}

function convertToPostfixExpression(fxInput) {
    const fx = fxInput.replace(/\s+/g, '');
    const operators = ['*', '+', '~', 'nor', 'nand', 'xor', 'xnor'];
    const limiters = ['(', ')'];
    const fxOperators = [];
    const fxVariables = [];
    const fxLimiters = [];
    const fxElements = [];

    for (let index = 0; index < fx.length; index++) {
        const character = fx[index];
        if (operators.indexOf(character) !== -1) {
            const operator = new Operator(character, index);
            fxOperators.push(operator);
        } else if(/^[A-Z]$/.test(character) || limiters.indexOf(character) !== -1) {
            const element = new Element(character, index);
            fxElements.push(element);
        }
    }

    fxElements.forEach(element => {
        if (element.character === '(' || element.character === ')') {
            fxLimiters.push(element);
        } else {
            fxVariables.push(element);
        }
    });

    console.log(fx);
    console.log(fxElements);
    console.log(fxOperators);
    console.log(fxVariables);
    console.log(fxLimiters);

    for (let index = 0; index < fxLimiters.length; index++) {
        if (fxLimiters[index].character === '(' && fxLimiters[index+1].character === '('){
            index = index + 1;
        }
        if (fxLimiters[index].character === '(' && fxLimiters[index+1].character === ')'){
            fxLimiters[index].setElement(fxLimiters[index+1]);
            fxLimiters[index+1].setElement(fxLimiters[index]);
        }
        /*
        if (fxLimiters[index].character === ')' && fxLimiters[index-1].character === '(') {
            fxLimiters[index].setElement(fxLimiters[index-1]);
            fxLimiters[index-1].setElement(fxLimiters[index]);
        }
        if (fxLimiters[index].character === ')' && fxLimiters[index-1].character === ')') {
            fxLimiters[index].setElement(fxLimiters[index-1].element);
        }*/
    }
}

convertToPostfixExpression("~((A + C) * (B + A)) + C * (D + E)");
