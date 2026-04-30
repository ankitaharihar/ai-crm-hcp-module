import { useSelector } from 'react-redux';

export default function App() {
  const interactionCount = useSelector((state) => state.interactions.items.length);

  return (
    <main>
      <h1>AI-First CRM</h1>
      <p>Interaction logs ready: {interactionCount}</p>
    </main>
  );
}