// async function analyzeDebate() {
//     const topic = document.getElementById('topic-input').value;
//     if (!topic) return;

//     // Show loading state
//     document.getElementById('pros-content').innerHTML = 'Analyzing...';
//     document.getElementById('cons-content').innerHTML = 'Analyzing...';
//     document.getElementById('verdict-content').innerHTML = 'Calculating...';

//     try {
//         const response = await fetch('/analyze', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ topic })
//         });

//         const data = await response.json();
        
//         document.getElementById('pros-content').innerHTML = data.pros;
//         document.getElementById('cons-content').innerHTML = data.cons;
//         document.getElementById('verdict-content').innerHTML = data.verdict;
//     } catch (error) {
//         console.error('Error:', error);
//     }
// }

async function analyzeDebate() {
    const topic = document.getElementById('topic-input').value;
    if (!topic) {
        alert('Please enter a topic');
        return;
    }
    document.getElementById('pros-content').innerHTML = 'Analyzing...';
    document.getElementById('cons-content').innerHTML = 'Analyzing...';
    document.getElementById('verdict-content').innerHTML = 'Calculating...';
    try {
        const response = await fetch('http://127.0.0.1:5000/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Unknown error');
        }
        


        const data = await response.json();
        console.log('Response:', data);

        document.getElementById('pros-content').innerText = data.pros || 'No data';
        document.getElementById('cons-content').innerText = data.cons || 'No data';
        document.getElementById('verdict-content').innerText = data.verdict || 'No verdict';
    } catch (err) {
        console.error('Error:', err);
        alert(`Error: ${err.message}`);
    }
}

