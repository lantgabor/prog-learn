// import { useState, useEffect } from "react";

// export default function Timer() {
//   const [seconds, setSeconds] = useState(0);
//   const [running, setRunning] = useState(false);

//   useEffect(() => {
//     if (!running) return;
//     const interval = setInterval(() => setSeconds((s) => s + 1), 1000);
//     return () => clearInterval(interval);
//   }, [running]);

//   return (
//     <div>
//       <h1 style={{color: "white"}}>
//         {new Date(seconds * 1000).toISOString().substr(11, 8)}
//       </h1>
//       <button onClick={() => setRunning(true)}>Start Timer</button>
//     </div>
//   );
// }

import { useState, useEffect } from "react";

export default function Timer() {
  const [seconds, setSeconds] = useState(() => {
    return parseInt(localStorage.getItem("timer-seconds")) || 0;
  });
  const [running, setRunning] = useState(() => {
    return localStorage.getItem("timer-running") === "true";
  });

  useEffect(() => {
    localStorage.setItem("timer-seconds", seconds);
  }, [seconds]);

  useEffect(() => {
    localStorage.setItem("timer-running", running);
  }, [running]);

  useEffect(() => {
    if (!running) return;
    const interval = setInterval(() => setSeconds((s) => s + 1), 1000);
    return () => clearInterval(interval);
  }, [running]);

  const formatTime = (totalSeconds) =>
    new Date(totalSeconds * 1000).toISOString().substr(11, 8);

  return (
    <div
      style={{
        position: "fixed",
        top: "20px",
        right: "20px",
        padding: "10px",
        border: "1px solid #ccc",
        borderRadius: "8px",
        boxShadow: "0 0 10px rgba(0,0,0,0.1)",
        zIndex: 1000,
      }}
    >
      <h1 style={{ color: "white" }}>{formatTime(seconds)}</h1>
      <button onClick={() => setRunning(true)}>Start Timer</button>
      <button
        onClick={() => {
          setRunning(false);
          setSeconds(0);
          localStorage.setItem("timer-seconds", "0");
          localStorage.setItem("timer-running", "false");
        }}
      >
        Reset
      </button>
    </div>
  );
}
