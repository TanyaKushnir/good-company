import React from 'react';
import Routes from './routes';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to Your Online Store</h1>
      </header>
      <main>
        <Routes />
      </main>
      <footer>
        <p>Footer content goes here.</p>
      </footer>
    </div>
  );
}

export default App;
