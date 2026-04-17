function processCouscous() {
    const input = document.getElementById('arrayInput').value;
    const algorithm = document.getElementById('algorithm').value;
    const arr = input.split(',').map(x => parseInt(x.trim()));
    
    // Имитация работы алгоритмов (в реальном проекте вызывали бы API)
    let result = [];
    
    switch(algorithm) {
        case 'symmetrical':
            result = symmetricalCouscous(arr);
            break;
        case 'chaotic':
            result = chaoticCouscous(arr);
            break;
        case 'golden':
            result = goldenCouscous(arr);
            break;
        case 'fractal':
            result = fractalCouscous(arr);
            break;
        case 'spiral':
            result = spiralCouscous(arr);
            break;
    }
    
    document.getElementById('result').innerHTML = `[${result.join(', ')}]`;
    animateCouscous();
}

function symmetricalCouscous(arr) {
    const result = [...arr];
    const n = result.length;
    const mid = Math.floor(n / 2);
    
    for (let i = 0; i < mid; i++) {
        if (i % 2 === 0) {
            [result[i], result[n - 1 - i]] = [result[n - 1 - i], result[i]];
        }
    }
    return result;
}

function chaoticCouscous(arr) {
    const result = [...arr];
    for (let i = result.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [result[i], result[j]] = [result[j], result[i]];
    }
    return result;
}

function goldenCouscous(arr) {
    const goldenRatio = (1 + Math.sqrt(5)) / 2;
    const result = new Array(arr.length);
    
    for (let i = 0; i < arr.length; i++) {
        const newIndex = Math.floor((i * goldenRatio) % arr.length);
        result[newIndex] = arr[i];
    }
    return result;
}

function fractalCouscous(arr) {
    if (arr.length <= 1) return arr;
    const mid = Math.floor(arr.length / 2);
    const left = fractalCouscous(arr.slice(0, mid));
    const right = fractalCouscous(arr.slice(mid)).reverse();
    return [...left, ...right];
}

function spiralCouscous(arr) {
    const result = [];
    let left = 0;
    let right = arr.length - 1;
    
    while (left <= right) {
        if (left === right) {
            result.push(arr[left]);
            break;
        }
        result.push(arr[right]);
        result.push(arr[left]);
        left++;
        right--;
    }
    return result;
}

function animateCouscous() {
    const animDiv = document.getElementById('animation');
    const emojis = ['🍝', '🍚', '✨', '🪞', '🌀'];
    let i = 0;
    
    animDiv.innerHTML = '';
    const interval = setInterval(() => {
        if (i > 10) {
            clearInterval(interval);
            animDiv.innerHTML = '🍝 Готово! 🍚';
            setTimeout(() => {
                animDiv.innerHTML = '';
            }, 2000);
        } else {
            animDiv.innerHTML = emojis[Math.floor(Math.random() * emojis.length)];
            i++;
        }
    }, 200);
}
