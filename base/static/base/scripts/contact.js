const labels = document.querySelectorAll('label')
const inputs = document.querySelectorAll('input')
const form = document.querySelector('form')
const textarea = document.querySelector('textarea')

const div1 = document.createElement('div')
const div2 = document.createElement('div')
const div3 = document.createElement('div')

div1.classList.add('form-control')
div1.appendChild(labels[0])
div1.appendChild(inputs[1])

div2.classList.add('form-control')
div2.appendChild(labels[1])
div2.appendChild(inputs[2])

div3.classList.add('form-control')
div3.appendChild(labels[2])
div3.appendChild(textarea)


form.appendChild(div1)
form.appendChild(div2)
form.appendChild(div3)

labels.forEach(label => {
  label.innerHTML = label.innerText
    .split('')
    .map((letter, idx) => `<span style="transition-delay:${idx * 50}ms">${letter}</span>`)
    .join('')
})