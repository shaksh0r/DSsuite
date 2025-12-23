import { useEffect, useState } from "react";
import "./App.css";

const API_BASE = "http://localhost:8080/linkedlist";

function App() {
  const [list, setList] = useState([]);
  const [value, setValue] = useState("");
  const [position, setPosition] = useState("");
  const [updateValue, setUpdateValue] = useState("");

  const fetchList = async () => {
    const res = await fetch(`${API_BASE}/full_list`);
    const data = await res.json();
    setList(data.list);
  };

  useEffect(() => {
    fetchList();
  }, []);

  const appendItem = async () => {
    if (value === "") return;
    await fetch(`${API_BASE}/append`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ item: value }),
    });
    setValue("");
    fetchList();
  };

  const removeItem = async () => {
    if (position === "") return;
    await fetch(`${API_BASE}/remove`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ position: Number(position) }),
    });
    setPosition("");
    fetchList();
  };

  const updateItem = async () => {
    if (position === "" || updateValue === "") return;
    await fetch(`${API_BASE}/update`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        position: Number(position),
        value: updateValue,
      }),
    });
    setPosition("");
    setUpdateValue("");
    fetchList();
  };

  return (
    <div className="container">
      <h1>Linked List Visualizer</h1>

      <div className="controls">
        <div>
          <input
            placeholder="Value"
            value={value}
            onChange={(e) => setValue(e.target.value)}
          />
          <button onClick={appendItem}>Append</button>
        </div>

        <div>
          <input
            placeholder="Position"
            value={position}
            onChange={(e) => setPosition(e.target.value)}
          />
          <button onClick={removeItem}>Remove</button>
        </div>

        <div>
          <input
            placeholder="Position"
            value={position}
            onChange={(e) => setPosition(e.target.value)}
          />
          <input
            placeholder="New Value"
            value={updateValue}
            onChange={(e) => setUpdateValue(e.target.value)}
          />
          <button onClick={updateItem}>Update</button>
        </div>
      </div>

      <div className="list">
        {list.length === 0 && <p className="empty">List is empty</p>}
        {list.map((item, index) => (
          <div className="node-wrapper" key={index}>
            <div className="node">
              <div className="index">{index}</div>
              <div className="value">{item}</div>
            </div>
            {index !== list.length - 1 && <div className="arrow">→</div>}
          </div>
        ))}
        {list.length > 0 && <div className="null">NULL</div>}
      </div>
    </div>
  );
}

export default App;
