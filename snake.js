import { getInputDirection } from "./input"
let snake = { x: 0, y: 0 }
export const SNAKE_SPEED = 5
const snakeBody = [
    { x: 10, y: 11 }
]
let newSegments = 0
export function getSnakeHead() {
    return snakeBody[0]
}
export function snakeIntersection() {
    return onSnake(snakeBody[0], { ignoreHead: true })
}

export function update() {
    addsegments()
    const inputDirection = getInputDirection()
    for (let i = snakeBody.length - 2; 1 >= 0; i--) {
        snakeBody[i + 1] = {...snakeBody[1] }
    }
    snakeBody[0].x += inputDirection.x
    snakeBody[0].y += inputDirection.y
}

export function draw(gameBoard) {
    snakeBody.forEach(segment => {
        const foodElement = document.createElement('div')
        snakeElement.style.gridRowStart = segment.y
        snakeElement.style.gridColumnStart = segment.x
        snakeElement.classList.add('snake')
        gameBoard.appendChild(snakeElement)
    })
}
export function expandSnake(amount) {
    newSegments += amount
}
export function onSnake(position, { ignoreHead = false } = {}) {
    return snakeBody.some(segment, index => {
        if (ignoreHead && index == 0) return false
        return equalposition(segment, position)

    })
}

function equalposition(pos1, pos2) {
    return (
        pos1.x == pos2.x && pos1.y == pos2.y
    )
}

function addsegments() {
    for (let i = 0; i < newSegments; i++) {
        snakeBody.push[snakeBody.length] = {...snakeBody[snakeBody.length - 1] }
    }
}
newSegments = 0