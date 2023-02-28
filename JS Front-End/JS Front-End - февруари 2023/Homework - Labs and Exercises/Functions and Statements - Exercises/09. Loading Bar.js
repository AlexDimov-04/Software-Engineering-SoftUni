function loadingBar(n) {
    if (n === 100) {
        console.log('100% Complete!')
        console.log('[%%%%%%%%%%]')
    } else {
        console.log(`${n}% [${'%'.repeat(n / 10)}${'.'.repeat(10 - (n / 10))}]`)
        console.log('Still loading...')
    }

}

