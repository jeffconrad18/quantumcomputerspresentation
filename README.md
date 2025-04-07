# Quantum Computers Presentation

A presentation created using [Manim](https://www.manim.community/) and [Manim-Slides](https://github.com/jeertmans/manim-slides) about quantum computers.

## Presentation

The presentation was created and presented using `manim-slides` by converting it into an HTML slideshow:

```sh
manim present.py Titel Gliederung Superposition Verschraenkung BitsVergleich Gatter Parallel TSP Multiversum Ionen Herausforderungen Willow Anwendung RSA Zahl Fazit Quellen && \
manim-slides convert Titel Gliederung Superposition Verschraenkung BitsVergleich Gatter Parallel TSP Multiversum Ionen Herausforderungen Willow Anwendung RSA Zahl Fazit Quellen presentation.py
```

## Presentation Overview

The presentation was given in **German**, and the notes are in German as well:

### Einstieg
- **Flipper Zero "Hacking"** → Rick Roll → Verbindung zu Quantencomputern

### Titel
- **Quantencomputer**

### Übersicht
- **Konzepte**, **Aufbau im Vergleich zu klassischen Computern**, **aktueller Stand**, **Einsatzmöglichkeiten**

### Wichtige Konzepte
- **Superposition:** Münze hochwerfen und fangen → Qubit kann gleichzeitig 0 und 1 sein
- **Verschränkung:** Quantenverschränkung, auch über große Distanzen

### Aufbau
- **Klassischer Computer vs. Quantencomputer** → Binärzahlen vs. Qubits → exponentielle Skalierung (`2^n`)
- **Logik:** Klassische Gatter (`UND`, `ODER`, usw.) vs. Quantengatter

### Anwendung
- **Labyrinth lösen:** Sequentiell vs. parallel → Google-Zitat "Parallelwelten"
- **Willow-Chip Aufbau** → Andere Quantencomputer-Designs
- **Probleme:** Dekohärenz, Skalierbarkeit
- **Nutzen:**
  - Simulationen (Physik, Materialforschung, Quanten-Chemie)
  - Optimierung (Logistik, Finanzwirtschaft)
  - Künstliche Intelligenz & Machine Learning (Grover's Algorithmus)
  - Kryptographie: **Shor-Algorithmus** zur Faktorisierung großer Zahlen → RSA nicht quantensicher

### Fazit
- **Großes Potenzial für bestimmte Aufgaben:** Bessere Batterien, neue Medikamente, AGI
- **Ersetzen klassische Computer nicht!**
- **Aktuelle Limitationen:** Anzahl logischer Qubits → Noch nicht einsatzbereit

## Quellen

- [DigiCert Post-Quantum Cryptography](https://www.digicert.com/de/insights/post-quantum-cryptography)
- [arXiv Paper (1905.09749)](https://arxiv.org/pdf/1905.09749)
- [PennyLane Quantum Machine Learning](https://pennylane.ai/qml/demos/tutorial_trapped_ions)
- [Photonworld Quantum Tech PDF](https://photonworld.de/uploads/tx_photonworld/pdf/tech-36-d-06-web.pdf)
- [Quarks - Quantencomputer FAQ](https://www.quarks.de/technik/faq-so-funktioniert-ein-quantencomputer/)
- [Google Blog - Willow Quantum Chip](https://blog.google/technology/research/google-willow-quantum-chip/)
- [Nature Quantum Computing Article](https://www.nature.com/articles/s41586-024-08449-y)
- [Karlsruhe Physics Course PDF](https://www.karlsruher-physikkurs.de/download/2024-05-31-quantencomputer-karlsruhe.pdf)
- **YouTube Videos:**
  - [Verständliche Einführung](https://www.youtube.com/watch?v=-UrdExQW0cs&list=WL&index=2)
  - [Quantencomputer einfach erklärt](https://www.youtube.com/watch?v=lvTqbM5Dq4Q&list=WL&index=1&pp=gAQBiAQB)
  - [Google’s Quantum Breakthrough](https://techhq.com/2025/01/google-quantum-breakthrough-marred-by-parallel-universe-claim/)
  - [Quantencomputer Grundlagen](https://www.youtube.com/watch?v=g_IaVepNDT4)
  - [Weitere Einblicke](https://www.youtube.com/watch?v=lDbP85k6Z-E&t=28s)
  - [Quantencomputer & Cybersicherheit](https://www.youtube.com/watch?v=rYW2NlU359U)

---

Feel free to fork and modify this presentation for your own use!
