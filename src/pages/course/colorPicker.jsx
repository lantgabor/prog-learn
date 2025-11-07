import { useEffect, useRef, useState } from "react";

export default function ColorPicker() {
  const canvasRef = useRef(null);
  const [rgb, setRgb] = useState([255, 0, 0]);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    // Draw color wheel with hue gradient (horizontal) and brightness gradient (vertical)
    const drawColorWheel = () => {
      const gradH = ctx.createLinearGradient(0, 0, canvas.width, 0);
      gradH.addColorStop(0, "rgb(255,0,0)");
      gradH.addColorStop(0.17, "rgb(255,255,0)");
      gradH.addColorStop(0.34, "rgb(0,255,0)");
      gradH.addColorStop(0.51, "rgb(0,255,255)");
      gradH.addColorStop(0.68, "rgb(0,0,255)");
      gradH.addColorStop(0.85, "rgb(255,0,255)");
      gradH.addColorStop(1, "rgb(255,0,0)");
      ctx.fillStyle = gradH;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      const gradV = ctx.createLinearGradient(0, 0, 0, canvas.height);
      gradV.addColorStop(0, "rgba(255,255,255,1)");
      gradV.addColorStop(0.5, "rgba(255,255,255,0)");
      gradV.addColorStop(0.5, "rgba(0,0,0,0)");
      gradV.addColorStop(1, "rgba(0,0,0,1)");
      ctx.fillStyle = gradV;
      ctx.fillRect(0, 0, canvas.width, canvas.height);
    };

    drawColorWheel();

    const handleColorPick = (e) => {
      const rect = canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const imageData = ctx.getImageData(x, y, 1, 1).data;
      setRgb([imageData[0], imageData[1], imageData[2]]);
    };

    canvas.addEventListener("click", handleColorPick);
    return () => canvas.removeEventListener("click", handleColorPick);
  }, []);

  const rgbString = `rgb(${rgb.join(",")})`;
  const rgbDisplay = `RGB(${rgb.join(", ")})`;

  return (
    <div style={{ textAlign: "center", marginTop: "2rem" }}>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          gap: "1rem",
          marginBottom: "1.5rem",
        }}
      >
        <div
          style={{
            width: "80px",
            height: "80px",
            border: "2px solid #333",
            borderRadius: "4px",
            backgroundColor: rgbString,
            boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
          }}
        />
        <h3 style={{ margin: 0 }}>{rgbDisplay}</h3>
      </div>

      <canvas
        ref={canvasRef}
        width={256}
        height={256}
        style={{
          border: "2px solid #333",
          borderRadius: "4px",
          cursor: "crosshair",
          display: "block",
          margin: "0 auto",
        }}
      />
    </div>
  );
}
