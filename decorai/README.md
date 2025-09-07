# 🪑 DecorAI: AI-Powered 3D Model Creator

Welcome to **DecorAI** — an intelligent tool for transforming product photos into accurate, lightweight 3D models, ready for AR visualization and AI-powered interior editing.

---

## 🚀 Features

- **Photo to 3D Model:** Convert product images into realistic 3D models using photogrammetry and AI.
- **AR Ready:** Export models in glTF, OBJ, or USDZ formats for seamless AR integration.
- **AI Interior Editing:** (Coming soon) Visualize customer prompts and redesign living spaces with generative AI.
- **Batch Processing:** Easily process multiple images at once.

---

## 🛠️ Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare Your Images

- Place product photos in the `input_images/` folder.
- Use multiple angles for best 3D results.

### 3. Generate 3D Models

```bash
python generate_3d_model.py
```
- Output models will be saved in the `output_models/` folder.

---

## 📦 Project Structure

```
decorai/
├── input_images/        # Place your product photos here
├── output_models/       # Generated 3D models (.glb, .obj, .usdz)
├── generate_3d_model.py # Main script for model generation
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ✨ Next Steps

- [ ] Integrate AR visualization (WebXR, ARKit, ARCore)
- [ ] Add AI-powered interior editing (Stable Diffusion, Stable 3D)
- [ ] Enhance UI/UX for customer interaction

---

## 📚 Resources

- [Stability AI Documentation](https://platform.stability.ai/docs/api-reference)
- [Meshroom Photogrammetry](https://alicevision.org/#meshroom)
- [glTF Viewer](https://gltf-viewer.donmccurdy.com/)

---

## 💡 Contributing

Pull requests and suggestions are welcome!  
Feel free to open issues for bugs, feature requests, or improvements.

---

## 📝 License

This project is licensed under the MIT License.

---

**DecorAI** — Bring your products to life in 3D and enhance your AR experiences.