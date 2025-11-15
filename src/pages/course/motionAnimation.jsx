import React, { useState } from 'react';

export function FrameByFrameDemo() {
  const [currentFrame, setCurrentFrame] = useState(0);
  const maxFrames = 10;
  const velocity = 30;

  const getPosition = (frame) => {
    return 50 + frame * velocity;
  };

  return (
    <div style={{
      border: '2px solid #ddd',
      borderRadius: '8px',
      padding: '1.5rem',
      backgroundColor: '#f9f9f9',
      marginBottom: '2rem'
    }}>
      <h4 style={{ marginTop: 0 }}>Animáció Képkockánként (Frame-by-Frame)</h4>

      <svg width="100%" height="200" style={{
        backgroundColor: '#fff',
        border: '1px solid #ccc',
        borderRadius: '4px'
      }}>
        {/* Grid with frame numbers */}
        {Array.from({ length: maxFrames + 1 }, (_, i) => {
          const x = 50 + i * velocity;
          return (
            <g key={i}>
              <line
                x1={x}
                y1="0"
                x2={x}
                y2="200"
                stroke={i === currentFrame ? "#ff6b6b" : "#e0e0e0"}
                strokeWidth={i === currentFrame ? "2" : "1"}
                strokeDasharray={i === currentFrame ? "5,5" : "none"}
              />
              <text
                x={x}
                y="190"
                textAnchor="middle"
                fontSize="11"
                fill={i === currentFrame ? "#ff0000" : "#666"}
                fontWeight={i === currentFrame ? "bold" : "normal"}
              >
                {i}
              </text>
            </g>
          );
        })}

        {/* Trail of previous positions */}
        {Array.from({ length: currentFrame }, (_, i) => {
          const x = getPosition(i);
          const opacity = 0.2 + (i / currentFrame) * 0.3;
          return (
            <circle
              key={i}
              cx={x}
              cy="100"
              r="15"
              fill="#ff9999"
              opacity={opacity}
            />
          );
        })}

        {/* Current position */}
        <circle
          cx={getPosition(currentFrame)}
          cy="100"
          r="20"
          fill="#ff4444"
          stroke="#cc0000"
          strokeWidth="2"
        />

        {/* Ground line */}
        <line x1="0" y1="100" x2="400" y2="100" stroke="#333" strokeWidth="1" opacity="0.3"/>

        {/* Frame label */}
        <text
          x={getPosition(currentFrame)}
          y="70"
          textAnchor="middle"
          fontSize="14"
          fill="#333"
          fontWeight="bold"
        >
          Frame {currentFrame}
        </text>
      </svg>

      <div style={{ marginTop: '1rem' }}>
        <label style={{ display: 'block', marginBottom: '0.5rem' }}>
          <strong>Képkocka (Frame):</strong> {currentFrame} / {maxFrames}
        </label>
        <input
          type="range"
          min="0"
          max={maxFrames}
          step="1"
          value={currentFrame}
          onChange={(e) => setCurrentFrame(parseInt(e.target.value))}
          style={{ width: '100%', marginBottom: '1rem' }}
        />

        <div style={{
          padding: '1rem',
          backgroundColor: '#fff3e0',
          borderRadius: '4px',
          fontSize: '0.9rem',
          marginBottom: '1rem'
        }}>
          <strong>Képlet:</strong><br/>
          <code style={{
            display: 'block',
            padding: '0.5rem',
            backgroundColor: '#fff',
            borderRadius: '4px',
            marginTop: '0.5rem'
          }}>
            pozíció = 50 + (frame × {velocity})<br/>
            pozíció = 50 + ({currentFrame} × {velocity}) = <strong>{getPosition(currentFrame)} pixel</strong>
          </code>
        </div>

        <div style={{
          padding: '1rem',
          backgroundColor: '#e1f5fe',
          borderRadius: '4px',
          fontSize: '0.9rem'
        }}>
          <strong>Mit látsz?</strong><br/>
          Az animáció valójában sok különálló képből (frame) áll. Minden frame-ben a labda
          {velocity} pixellel arrébb kerül. Amikor ezeket gyorsan egymás után mutatjuk
          (általában 60 frame/másodperc), a szemünk összeolvasztja őket, és <strong>folyamatos
          mozgást</strong> látunk!
        </div>
      </div>
    </div>
  );
}
