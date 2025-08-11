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
    <div style={{ padding: '20px', maxWidth: '600px', margin: '0 auto' }}>
      <h1>Query→Answer App</h1>
      <div>
        <label htmlFor="query">Query</label>
        <textarea
          id="query"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter your query here..."
          rows="4"
          style={{ width: '100%', marginBottom: '10px' }}
          required
        />
      </div>
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? 'Loading...' : 'Send'}
      </button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div style={{ marginTop: '20px' }}>
        <label htmlFor="answer">Answer</label>
        <textarea
          id="answer"
          value={answer}
          readOnly
          placeholder="Answer will appear here..."
          rows="4"
          style={{ width: '100%', background: '#f0f0f0' }}
        />
      </div>
    </div>
  );
}

export default App;