import { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    setAnswer('');
    
    try {
      const response = await fetch('http://localhost:8000/api/answer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query }),
      });
      
      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.detail || 'Failed to fetch answer');
      }
      
      setAnswer(data.answer);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>ChatIG</h1>
      
      <div className="query-container">
        <label htmlFor="query">Query</label>
        <textarea
          id="query"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter your query here..."
          required
        />
        <span className="char-count">{query.length}/2000</span>
      </div>

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? 'Loading...' : 'Send'}
      </button>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      <div className="answer-container">
        <label htmlFor="answer">Answer</label>
        <textarea
          id="answer"
          value={answer}
          readOnly
          placeholder="Answer will appear here..."
        />
      </div>
    </div>
  );
}

export default App;