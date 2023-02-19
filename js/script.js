const toggleSectionText = (section, btnText1, btnText2, parText1, parText2) => {
    const btn = section.querySelector('input')
    const par = section.querySelector('p')

    if (btn.value === btnText1) {
        btn.value = btnText2
        par.textContent = parText2
    } else {
        btn.value = btnText1
        par.textContent = parText1
    }
}


const window1 = document.querySelector('#window');
window1.addEventListener('click', () => toggleSectionText(window1, 'Открыть форточку', 'Закрыть форточку', 
'Форточка закрыта', 'Форточка открыта'
));

const hum1 = document.querySelector('#hum');
hum1.addEventListener('click', () => toggleSectionText(hum1, 'Выключить увлажнение', 'Включить увлажнение', 
'Увлажнение воздуха включено','Увлажнение воздуха выключено '
))


const wat1 = document.querySelector('#wat');
wat1.addEventListener('click', () => toggleSectionText(wat1, 'Выключить полив', 'Включить полив', 
'Полив почвы включён', 'Полив почвы выключен'

))


const wat21 = document.querySelector('#wat2');
wat21.addEventListener('click', () => toggleSectionText(wat21, 'Выключить полив', 'Включить полив', 
'Полив почвы включён', 'Полив почвы выключен'

))


const wat31 = document.querySelector('#wat3');
wat31.addEventListener('click', () => toggleSectionText(wat31, 'Выключить полив', 'Включить полив', 
'Полив почвы включён', 'Полив почвы выключен'

))


const wat41 = document.querySelector('#wat4');
wat41.addEventListener('click', () => toggleSectionText(wat41, 'Выключить полив', 'Включить полив', 
'Полив почвы включён', 'Полив почвы выключен'

))

const wat51 = document.querySelector('#wat5');
wat51.addEventListener('click', () => toggleSectionText(wat51, 'Выключить полив', 'Включить полив', 
'Полив почвы включён', 'Полив почвы выключен'

))

const wat61 = document.querySelector('#wat6');
wat61.addEventListener('click', () => toggleSectionText(wat61, 'Выключить полив', 'Включить полив', 
'Полив почвы включён', 'Полив почвы выключен'

))
