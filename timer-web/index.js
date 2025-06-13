const { useState, useEffect, useRef } = React;

function App() {
  const [timer, setTimer] = useState(0);
  const [shouldTime, setShouldTime] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const audioRef = useRef(null);

  useEffect(() => {
    let interval;
    if (shouldTime && !isPaused) {
      interval = setInterval(() => {
        setTimer(prev => {
          if (prev <= 0.1) {
            clearInterval(interval);
            if (audioRef.current) {
              audioRef.current.currentTime = 0;
              audioRef.current.play();
            }
            return 0;
          }
          return parseFloat((prev - 0.1).toFixed(1));
        });
      }, 100);
    }
    return () => clearInterval(interval);
  }, [shouldTime, isPaused]);

  const resetTimer = duration => {
    setTimer(duration);
    setShouldTime(true);
    setIsPaused(false);
    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.currentTime = 0;
    }
  };

  useEffect(() => {
    const handleKey = e => {
      switch (e.key.toLowerCase()) {
        case 'r':
          resetTimer(10);
          break;
        case 'm':
          resetTimer(30);
          break;
        case 'b':
          resetTimer(5);
          break;
        case 'p':
          setShouldTime(false);
          break;
        case 'x':
          setIsPaused(p => !p);
          break;
        default:
      }
    };
    window.addEventListener('keydown', handleKey);
    return () => window.removeEventListener('keydown', handleKey);
  }, []);

  return (
    React.createElement('div', {
        style: {
          height: '100%',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
          backgroundColor: shouldTime && timer < 3 ? 'firebrick' : 'white'
        }
      },
      shouldTime && React.createElement('h1', { style: { fontSize: '5rem', margin: 0 } }, timer.toFixed(1)),
      React.createElement('div', null,
        React.createElement('button', { onClick: () => resetTimer(10) }, 'Standard (R)'),
        React.createElement('button', { onClick: () => resetTimer(30) }, 'Computation (M)'),
        React.createElement('button', { onClick: () => resetTimer(5) }, 'Bounce Back (B)'),
        React.createElement('button', { onClick: () => setShouldTime(false) }, 'Clear (P)'),
        React.createElement('button', { onClick: () => setIsPaused(p => !p) }, isPaused ? 'Resume (X)' : 'Pause (X)')
      ),
      React.createElement('audio', { ref: audioRef, src: 'Scorekeeper/buzz.mp3' })
    )
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(React.createElement(App));
