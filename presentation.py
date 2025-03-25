from manim import *
import numpy as np

class QuantumSuperposition3D(ThreeDScene):
    def construct(self):
        # Set up camera
        self.set_camera_orientation(phi=70*DEGREES, theta=-30*DEGREES)
        
        # Create title in a dedicated region
        title = Text("Quantum Superposition Visualized", color=WHITE).scale(0.8)
        title.to_corner(UP)
        self.add_fixed_in_frame_mobjects(title)
        
        # Create info box for explanations
        info_box = Rectangle(width=6, height=2, color=WHITE, fill_opacity=0.1)
        info_box.to_corner(DR)
        info_text = Text("", color=WHITE).scale(0.4)
        info_text.move_to(info_box.get_center())
        
        self.add_fixed_in_frame_mobjects(info_box)
        self.add_fixed_in_frame_mobjects(info_text)
        
        # Create axes
        axes = ThreeDAxes()
        
        # Create Bloch sphere
        bloch_sphere = Sphere(radius=2, resolution=(20, 20))
        bloch_sphere.set_color(BLUE)
        bloch_sphere.set_opacity(0.2)
        
        # Show the basic setup with explanation
        self.update_info_text(info_text, "The Bloch sphere is a geometric\nrepresentation of a qubit's state")
        self.play(Create(axes), Create(bloch_sphere))
        self.wait()
        
        # Add axis labels with better positioning
        x_label = Text("|0⟩", color=RED).scale(0.7)
        y_label = Text("|1⟩", color=GREEN).scale(0.7)
        z_label = Text("Phase", color=BLUE).scale(0.7)
        
        x_label.move_to(2.5*RIGHT)
        y_label.move_to(2.5*UP)
        z_label.move_to(2.5*OUT)
        
        self.add_fixed_in_frame_mobjects(x_label)
        self.add_fixed_in_frame_mobjects(y_label)
        self.add_fixed_in_frame_mobjects(z_label)
        
        # Create a separate area for bit explanation
        bit_box = Rectangle(width=6, height=1, color=YELLOW, fill_opacity=0.1)
        bit_box.to_edge(DOWN)
        bit_text = Text("Classical Bit: 0 OR 1", color=YELLOW).scale(0.6)
        bit_text.move_to(bit_box.get_center())
        
        self.add_fixed_in_frame_mobjects(bit_box)
        self.add_fixed_in_frame_mobjects(bit_text)
        
        # Create vectors for the basis states
        basis_0_vector = [2, 0, 0]
        basis_1_vector = [0, 2, 0]
        
        # Create line for |0⟩ state
        state_0 = Line(ORIGIN, basis_0_vector, color=RED)
        state_0_dot = Sphere(radius=0.1).move_to(basis_0_vector)
        state_0_dot.set_color(RED)
        
        # Show |0⟩ state with updated info
        self.update_info_text(info_text, "Classical state |0⟩\nOne of the basis states")
        self.play(Create(state_0), Create(state_0_dot))
        self.wait()
        
        # Create line for |1⟩ state
        state_1 = Line(ORIGIN, basis_1_vector, color=GREEN)
        state_1_dot = Sphere(radius=0.1).move_to(basis_1_vector)
        state_1_dot.set_color(GREEN)
        
        # Show |1⟩ state with updated info
        self.update_info_text(info_text, "Classical state |1⟩\nThe other basis state")
        self.play(Create(state_1), Create(state_1_dot))
        self.wait()
        
        # Update bit explanation
        new_bit_text = Text("Quantum Bit (Qubit): 0 AND 1", color=YELLOW).scale(0.6)
        new_bit_text.move_to(bit_box.get_center())
        
        self.play(FadeOut(bit_text), FadeIn(new_bit_text))
        bit_text = new_bit_text
        
        # Create a superposition state
        superposition_vector = [1.414, 1.414, 0]  # Equal superposition
        superposition_state = Line(ORIGIN, superposition_vector, color=YELLOW)
        superposition_dot = Sphere(radius=0.15).move_to(superposition_vector)
        superposition_dot.set_color(YELLOW)
        
        # Update info for superposition
        self.update_info_text(info_text, "Superposition state\n|ψ⟩ = (|0⟩ + |1⟩)/√2\nExists in BOTH states at once")
        
        # Create an animation showing superposition forming
        self.play(
            Transform(state_0, superposition_state),
            Transform(state_1, superposition_state.copy()),
            Transform(state_0_dot, superposition_dot),
            Transform(state_1_dot, superposition_dot.copy())
        )
        self.wait()
        
        # Rotate camera to see 3D effect
        self.move_camera(phi=75*DEGREES, theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        # Show measurement concept
        new_bit_text = Text("Measurement collapses superposition", color=WHITE).scale(0.6)
        new_bit_text.move_to(bit_box.get_center())
        self.play(FadeOut(bit_text), FadeIn(new_bit_text))
        bit_text = new_bit_text
        self.wait()
        
        # Show collapse to |0⟩
        collapse_to_0 = Line(ORIGIN, basis_0_vector, color=RED)
        collapse_to_0_dot = Sphere(radius=0.1).move_to(basis_0_vector)
        collapse_to_0_dot.set_color(RED)
        
        self.update_info_text(info_text, "Measurement outcome: |0⟩\nRandom with 50% probability")
        
        self.play(
            Transform(state_0, collapse_to_0),
            Transform(state_1, collapse_to_0.copy()),
            Transform(state_0_dot, collapse_to_0_dot),
            Transform(state_1_dot, collapse_to_0_dot.copy())
        )
        self.wait(2)
        
        # Reset to superposition to show another possible outcome
        self.update_info_text(info_text, "Superposition state\n|ψ⟩ = (|0⟩ + |1⟩)/√2\nBefore measurement")
        
        self.play(
            Transform(state_0, superposition_state),
            Transform(state_1, superposition_state.copy()),
            Transform(state_0_dot, superposition_dot),
            Transform(state_1_dot, superposition_dot.copy())
        )
        self.wait()
        
        # Show collapse to |1⟩
        collapse_to_1 = Line(ORIGIN, basis_1_vector, color=GREEN)
        collapse_to_1_dot = Sphere(radius=0.1).move_to(basis_1_vector)
        collapse_to_1_dot.set_color(GREEN)
        
        self.update_info_text(info_text, "Measurement outcome: |1⟩\nRandom with 50% probability")
        
        self.play(
            Transform(state_0, collapse_to_1),
            Transform(state_1, collapse_to_1.copy()),
            Transform(state_0_dot, collapse_to_1_dot),
            Transform(state_1_dot, collapse_to_1_dot.copy())
        )
        self.wait(2)
        
        # Final explanation
        final_text = Text("Quantum superposition allows a qubit to exist\nin multiple states until measured", 
                          color=WHITE).scale(0.6)
        final_text.move_to(bit_box.get_center())
        self.play(FadeOut(bit_text), FadeIn(final_text))
        
        # Move camera to final position for conclusion
        self.move_camera(phi=70*DEGREES, theta=30*DEGREES)
        self.wait(2)
    
    def update_info_text(self, text_obj, new_text):
        """Helper function to update the information text"""
        new_text_obj = Text(new_text, color=WHITE).scale(0.4)
        new_text_obj.move_to(text_obj.get_center())
        self.play(FadeOut(text_obj), FadeIn(new_text_obj))
        text_obj.become(new_text_obj)




#######################

class QuantumEntanglementScene(Scene):
    def construct(self):
        # Create two circles to represent the entangled particles, placing them apart.
        left_particle = Circle(radius=0.7, color=BLUE).shift(LEFT * 3)
        right_particle = Circle(radius=0.7, color=BLUE).shift(RIGHT * 3)

        # Add a title to introduce the concept.
        title = Text("Visualizing Quantum Entanglement", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Show both particles in an indeterminate (superposition) state with a pulsating fill.
        self.play(
            FadeIn(left_particle),
            FadeIn(right_particle),
            left_particle.animate.set_fill(BLUE, opacity=0.4),
            right_particle.animate.set_fill(BLUE, opacity=0.4),
            run_time=2
        )
        self.wait(1)

        # Animate the particles’ superposition by having them gently change colors.
        self.play(
            left_particle.animate.set_fill(RED, opacity=0.6),
            right_particle.animate.set_fill(GREEN, opacity=0.6),
            run_time=2
        )
        self.wait(1)

        # Simulate the measurement on the left particle:
        # It "locks" into a stable, definite state (here represented by switching to a bright blue).
        self.play(left_particle.animate.set_fill(BLUE, opacity=1))
        self.wait(0.5)

        # Because of entanglement, the right particle must correlate with the left.
        # Instantly, the right particle also transitions to the same state.
        self.play(right_particle.animate.set_fill(BLUE, opacity=1))
        self.wait(1)

        # Optionally, emphasize the connection with a line or pulse between the two particles.
        connection = Line(left_particle.get_center(), right_particle.get_center(), color=YELLOW)
        self.play(Create(connection), run_time=1)
        self.wait(1)
        
        
from manim import *
import numpy as np

class SuperpositionSlide(ThreeDScene):
    def construct(self):
        # Kamera-Einstellung
        self.set_camera_orientation(phi=70*DEGREES, theta=-30*DEGREES)
        
        # Überschrift (fixiert im Bildschirmrahmen)
        title = Text("Superposition", font_size=48, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        
        # Koordinatensystem erstellen
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=4.5,
            y_length=4.5,
            z_length=4.5
        )
        self.add(axes)
        
        # Achsenbeschriftungen
        x_label = Text("|0⟩", color=RED).scale(0.7)
        y_label = Text("|1⟩", color=GREEN).scale(0.7)
        
        x_label.move_to(axes.c2p(0, -3.2, 0))
        y_label.move_to(axes.c2p(0, 3.2, 0))
        
        self.add_fixed_in_frame_mobjects(x_label, y_label)
        
        # Bloch-Kugel
        bloch_sphere = Sphere(radius=1.5, resolution=(20, 20))
        bloch_sphere.set_color(BLUE)
        bloch_sphere.set_opacity(0.2)
        self.add(bloch_sphere)
        
        # Trennebene hinzufügen
        plane = Surface(
            lambda u, v: axes.c2p(u, v, 0),
            u_range=[-2.5, 2.5],
            v_range=[-2.5, 2.5],
            checkerboard_colors=[BLUE_D, BLUE_E],
            fill_opacity=0.2
        )
        self.add(plane)
        
        # Zustandsbeschriftungen
        state_0 = Text("|0⟩", color=RED).scale(0.7).move_to(axes.c2p(0, 0, -2.5))
        state_1 = Text("|1⟩", color=GREEN).scale(0.7).move_to(axes.c2p(0, 0, 2.5))
        self.add_fixed_in_frame_mobjects(state_0, state_1)
        
        # Pfeil (Zustandsvektor)
        arrow = Arrow3D(
            start=ORIGIN,
            end=[0, 0, 2],
            color=YELLOW,
            thickness=0.05
        )
        self.add(arrow)
        
        # Superpositionsformel (fixiert im Bildschirmrahmen)
        formula = MathTex(r"|\psi\rangle = \alpha|0\rangle + \beta|1\rangle", font_size=36)
        formula.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(formula)
        
        # Animation des Pfeils (Superposition)
        def update_arrow(mob, dt):
            t = self.time % 4
            # Komplexere Bewegung für bessere Visualisierung
            theta = t * TAU  # Volle Drehung in der XY-Ebene
            phi = np.sin(t * PI) * PI/2  # Oszillation in Z-Richtung
            
            x = 1.5 * np.sin(phi) * np.cos(theta)
            y = 1.5 * np.sin(phi) * np.sin(theta)
            z = 1.5 * np.cos(phi)
            
            new_end = [x, y, z]
            mob.become(Arrow3D(start=ORIGIN, end=new_end, color=YELLOW, thickness=0.05))
        
        arrow.add_updater(update_arrow)
        self.wait(4)  # 4 Sekunden Superposition
        
        # Kollaps der Wellenfunktion
        arrow.clear_updaters()
        
        # Zufälligen Endzustand wählen (hier: |0⟩ oder |1⟩)
        final_state = np.random.choice([0, 1])
        collapsed_vector = [0, 0, 2] if final_state else [0, 0, -2]
        collapsed_arrow = Arrow3D(
            start=ORIGIN,
            end=collapsed_vector,
            color=GREEN if final_state else RED,
            thickness=0.05
        )
        
        # Kollaps-Label
        collapsed_label = Text(f"Kollabierter Zustand: |{final_state}⟩", 
                               color=GREEN if final_state else RED).scale(0.6)
        collapsed_label.to_corner(DR)
        self.add_fixed_in_frame_mobjects(collapsed_label)
        
        # Animation des Kollapses
        self.play(Transform(arrow, collapsed_arrow))
        self.wait(2)



from manim import *

class Title(Scene):
    def construct(self):
        title = Text("Quantencomputer", font_size=72)
        self.play(Write(title))
        self.wait(2)
        
from manim import *

class Gliederung(Scene):
    def construct(self):
        # Titel
        title = Text("Gliederung", font_size=48)
        title.to_edge(UP)
        underline = Line(title.get_left(), title.get_right(), color=WHITE)
        underline.next_to(title, DOWN, buff=0.1)
        
        # Gliederungspunkte
        points = VGroup(
            Text("1. Grundlagen"),
            Text("2. Aufbau"),
            Text("3. Aktueller Stand"),
            Text("4. Einsatzmöglichkeiten"),
            Text("5. Fazit")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        points.next_to(underline, DOWN, buff=0.5)
        
        # Animation
        self.play(Write(title))
        self.play(Create(underline))
        self.wait(0.5)
        for point in points:
            self.play(FadeIn(point, shift=UP*0.5))
            self.wait(0.3)
        
        self.wait(2)
        
        
        
class Quantenverschraenkung(ThreeDScene):
    def construct(self):
        # Kamera-Einstellung
        self.set_camera_orientation(phi=70*DEGREES, theta=-90*DEGREES, zoom=0.8)
        
        # Überschrift
        title = Text("Quantenverschränkung", font_size=48).to_edge(UP, buff=0.3)
        underline = Line(title.get_left(), title.get_right(), color=WHITE)
        underline.next_to(title, DOWN, buff=0.1)
        self.add_fixed_in_frame_mobjects(title, underline)
        self.play(Write(title), Create(underline))
        
        # Einstein-Zitat
        einstein_quote = Text(
            '"Spukhafte Fernwirkung"\n- Albert Einstein', 
            font_size=36, color=YELLOW, font="Italic"
        ).scale(1.2)
        self.add_fixed_in_frame_mobjects(einstein_quote)
        self.play(FadeIn(einstein_quote))
        self.wait(2)
        self.play(FadeOut(einstein_quote))
        
        # Quantensysteme
        axes_left = ThreeDAxes(x_range=[-2,2], y_range=[-2,2], z_range=[-2,2], 
                               x_length=3, y_length=3, z_length=3).shift(LEFT*5)
        axes_right = ThreeDAxes(x_range=[-2,2], y_range=[-2,2], z_range=[-2,2], 
                                x_length=3, y_length=3, z_length=3).shift(RIGHT*5)
        
        # Bloch-Kugeln
        sphere_left = Sphere(radius=1, resolution=20).set_color(BLUE).set_opacity(0.2)
        sphere_right = Sphere(radius=1, resolution=20).set_color(BLUE).set_opacity(0.2)
        sphere_left.move_to(axes_left.get_origin())
        sphere_right.move_to(axes_right.get_origin())
        
        # Trennebenen
        plane_left = Surface(
            lambda u, v: axes_left.c2p(u, v, 0),
            u_range=[-1.5, 1.5], v_range=[-1.5, 1.5],
            checkerboard_colors=[BLUE_D, BLUE_E],
            fill_opacity=0.2
        )
        plane_right = Surface(
            lambda u, v: axes_right.c2p(u, v, 0),
            u_range=[-1.5, 1.5], v_range=[-1.5, 1.5],
            checkerboard_colors=[BLUE_D, BLUE_E],
            fill_opacity=0.2
        )
        
        # Zustandsbeschriftungen
        for axes in [axes_left, axes_right]:
            self.add_fixed_in_frame_mobjects(
                Text("|0⟩", color=RED).scale(0.7).next_to(axes.z_axis, DOWN),
                Text("|1⟩", color=GREEN).scale(0.7).next_to(axes.z_axis, UP)
            )
        
        # Pfeile
        arrow_left = Arrow3D(start=axes_left.get_origin(), end=axes_left.c2p(0,0,0.9), color=RED, thickness=0.05)
        arrow_right = Arrow3D(start=axes_right.get_origin(), end=axes_right.c2p(0,0,0.9), color=GREEN, thickness=0.05)
        
        # Verbindung zwischen Quanten
        connection_line = DashedLine(axes_left.get_origin(), axes_right.get_origin(), color=WHITE)
        distance_label = Text("Distanz: ∞", font_size=24).next_to(connection_line, UP)
        
        
        # Bell-Zustand Formel
        bell_state = MathTex(r"|\psi\rangle = \frac{1}{\sqrt{2}}(|0\rangle|1\rangle - |1\rangle|0\rangle)", font_size=28).to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(bell_state)
        
        # Aufbau der Szene
        self.play(
            Create(axes_left), Create(axes_right),
            Create(sphere_left), Create(sphere_right),
            Create(plane_left), Create(plane_right)
        )
        self.wait(2)
        self.play(
            Create(connection_line), Write(distance_label),
            Write(bell_state)
        )
        self.add_fixed_in_frame_mobjects(distance_label)
        self.add(arrow_left, arrow_right)
        
        # Zufällige Bewegung der Pfeile
        def update_arrows(mob1, mob2, dt):
            t = self.time % 4
            angle1 = np.random.uniform(0, PI)
            angle2 = PI - angle1  # Gegenläufige Bewegung
            
            end_left = [np.sin(angle1), 0, np.cos(angle1)]
            end_right = [np.sin(angle2), 0, np.cos(angle2)]
            
            mob1.become(Arrow3D(start=axes_left.get_origin(), end=axes_left.c2p(*end_left), color=RED, thickness=0.05))
            mob2.become(Arrow3D(start=axes_right.get_origin(), end=axes_right.c2p(*end_right), color=GREEN, thickness=0.05))
        
        arrow_left.add_updater(lambda m, dt: update_arrows(m, arrow_right, dt))
        self.wait(4)
        
        # Kollaps der Wellenfunktion
        arrow_left.clear_updaters()
        collapse_state = np.random.choice([0, 1])
        collapse_left = [0, 0, 0.9] if collapse_state else [0, 0, -0.9]
        collapse_right = [0, 0, -0.9] if collapse_state else [0, 0, 0.9]
        
        collapsed_arrow_left = Arrow3D(start=axes_left.get_origin(), end=axes_left.c2p(*collapse_left), 
                                       color=RED if collapse_state else GREEN, thickness=0.05)
        collapsed_arrow_right = Arrow3D(start=axes_right.get_origin(), end=axes_right.c2p(*collapse_right), 
                                        color=GREEN if not collapse_state else RED, thickness=0.05)
        
        self.play(
            Transform(arrow_left, collapsed_arrow_left),
            Transform(arrow_right, collapsed_arrow_right),
            Flash(axes_left.get_origin(), line_length=0.3, num_lines=8, color=YELLOW, flash_radius=0.5, run_time=1)
        )
        
        # Endzustand anzeigen
        state_left = Text(f"|{collapse_state}⟩", color=RED if collapse_state else GREEN, font_size=24).next_to(axes_left, DOWN)
        state_right = Text(f"|{1-collapse_state}⟩", color=GREEN if collapse_state else RED, font_size=24).next_to(axes_right, DOWN)
        
        self.add_fixed_in_frame_mobjects(state_left, state_right)
        self.play(Write(state_left), Write(state_right))
        self.wait(3)


from manim import *

class BitsVergleich(Scene):
    def construct(self):
        # Titel und Unterstrich
        title = Text("Aufbau", font_size=48).to_edge(UP, buff=0.3)
        underline = Line(title.get_left(), title.get_right(), color=WHITE)
        underline.next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline))
        
        # Überschriften für die Tabelle
        computer_heading = Text("Computer", font_size=36).move_to([-3, 2, 0])
        quantum_heading = Text("Quantencomputer", font_size=36).move_to([3, 2, 0])
        
        self.play(
            Write(computer_heading),
            Write(quantum_heading)
        )
        
        # Visueller Vergleich von Bits vs Qubits
        # Klassische Bit-Darstellung (0 oder 1)
        bit_title = Text("Bits", font_size=30).move_to([-3, 0.9, 0])
        
        bit_0 = Circle(radius=0.5, color=WHITE, fill_opacity=0).move_to([-4, -0.5, 0])
        bit_0_label = Text("0", font_size=24).move_to(bit_0.get_center())
        
        bit_1 = Circle(radius=0.5, color=WHITE, fill_opacity=0).move_to([-2, -0.5, 0])
        bit_1_label = Text("1", font_size=24).move_to(bit_1.get_center())
        
        bit_arrow = Arrow(start=[-3, -1.5, 0], end=[-3, -2, 0])
        bit_state = Text("Entweder 0 oder 1", font_size=24).move_to([-3, -2.5, 0])
        
        # Quantum Bit (Qubit) Darstellung als Bloch-Kugel
        qubit_title = Text("Qubits", font_size=30).move_to([3, 0.9, 0])
        
        # Erstellen Sie eine ManimObject-Gruppe für das Qubit
        qubit_group = VGroup()
        
        # 3D-Elemente in einer 2D-Szene simulieren
        # Bloch-Kugel (als Kreis mit Ellipse für 3D-Effekt)
        bloch_sphere = Circle(radius=0.8, color=BLUE, fill_opacity=0.2).move_to([3, -0.7, 0])
        bloch_sphere_ellipse = Ellipse(width=2, height=0.5, color=BLUE, fill_opacity=0.1).move_to([3, -0.7, 0])
        
        # Z-Achse (vertikal)
        z_axis = Line(start=[3, -1.7, 0], end=[3, 0.3, 0], color=WHITE)
        z_top = Text("|1⟩", font_size=20, color=GREEN).next_to(z_axis, UP, buff=0.1)
        z_bottom = Text("|0⟩", font_size=20, color=RED).next_to(z_axis, DOWN, buff=0.1)
        
        # X-Achse
        x_axis = Line(start=[2, -0.7, 0], end=[4, -0.7, 0], color=WHITE)
        
        # Y-Achse (mit Tiefeneffekt)
        y_axis = Line(start=[3, -0.4, 0], end=[3, -1, 0], color=WHITE)
        
        # Zustandsvektor/Pfeil
        arrow = Arrow(start=[3, -0.7, 0], end=[3.7, -0.2, 0], color=YELLOW, buff=0)
        
        # Qubit-Zustandsbeschreibung
        qubit_arrow = Arrow(start=[3, -1.5, 0], end=[3, -2, 0])
        qubit_state = Text("Superposition", font_size=24).move_to([3, -2.5, 0])
        
        qubit_group.add(bloch_sphere, bloch_sphere_ellipse, z_axis, x_axis, y_axis, 
                      z_top, z_bottom, arrow, qubit_arrow, qubit_state)
        
        # Bits anzeigen
        self.play(Write(bit_title))
        self.play(Create(bit_0), Write(bit_0_label), Create(bit_1), Write(bit_1_label))
        self.play(Create(bit_arrow), Write(bit_state))
        self.wait(2)
        # Qubit anzeigen
        self.play(Write(qubit_title))
        self.play(
            Create(bloch_sphere),
            Create(bloch_sphere_ellipse),
            Create(z_axis),
            Create(x_axis),
            Create(y_axis),
            Write(z_top),
            Write(z_bottom)
        )
        self.play(Create(arrow))
        self.play(Create(qubit_arrow), Write(qubit_state))
        
        # Animation des Pfeils/Zustandsvektors mit mehr Bewegung nach unten
        def arrow_updater(mob, dt):
            t = self.renderer.time % 4  # Gesamter Animationszyklus: 4 Sekunden
            
            # Bewegung auf der Bloch-Kugel simulieren
            theta = t * TAU / 4  # Rotation in der XY-Ebene
            
            # Mehr Bewegung nach unten durch angepasste Oszillation
            phi = np.sin(t * PI) * PI/2 - PI/6  # Oszillation mit Bias nach unten
            
            # Kugel zu 2D projizieren
            x = 0.9 * np.sin(phi) * np.cos(theta)
            y = 0.9 * np.sin(phi) * np.sin(theta) * 0.5  # Elliptische Projektion
            z = 0.9 * np.cos(phi)
            
            # Pfeil aktualisieren
            new_end = [3 + x, -0.7 + z, 0]
            mob.put_start_and_end_on([3, -0.7, 0], new_end)
        
        arrow.add_updater(arrow_updater)
        
        self.wait(8)  # Animation für 8 Sekunden laufen lassen
        
        # Updater entfernen, wenn nicht mehr benötigt
        arrow.remove_updater(arrow_updater)


class QubitVisualization(ThreeDScene):
    def construct(self):
        # Kamera-Einstellung
        self.set_camera_orientation(phi=70*DEGREES, theta=-30*DEGREES)
        
        # Titel "Aufbau"
        title = Text("Aufbau", font_size=48, color=WHITE)
        title.to_edge(UP)
        underline = Line(title.get_left(), title.get_right(), color=WHITE)
        underline.next_to(title, DOWN, buff=0.1)
        self.add_fixed_in_frame_mobjects(title, underline)
        self.play(Write(title), Create(underline))
        
        # Überschriften für die Tabelle
        computer_heading = Text("Computer", font_size=36).to_corner(UL, buff=1)
        quantum_heading = Text("Quantencomputer", font_size=36).to_corner(UR, buff=1)
        self.add_fixed_in_frame_mobjects(computer_heading, quantum_heading)
        self.play(Write(computer_heading), Write(quantum_heading))
        
        # Bits auf der linken Seite (fixiert im Bildschirmrahmen)
        bit_title = Text("Bits", font_size=30).move_to([-4, 0, 0])
        
        bit_0 = Circle(radius=0.5, color=WHITE, fill_opacity=0).move_to([-5, -1, 0])
        bit_0_label = Text("0", font_size=24).move_to(bit_0.get_center())
        
        bit_1 = Circle(radius=0.5, color=WHITE, fill_opacity=0).move_to([-3, -1, 0])
        bit_1_label = Text("1", font_size=24).move_to(bit_1.get_center())
        
        bit_arrow = Arrow(start=[-4, -2, 0], end=[-4, -2.5, 0])
        bit_state = Text("Entweder 0 oder 1", font_size=24).move_to([-4, -3, 0])
        
        self.add_fixed_in_frame_mobjects(bit_title, bit_0, bit_0_label, bit_1, 
                                          bit_1_label, bit_arrow, bit_state)
        
        self.play(Write(bit_title))
        self.play(Create(bit_0), Write(bit_0_label), Create(bit_1), Write(bit_1_label))
        self.play(Create(bit_arrow), Write(bit_state))
        
        # Qubit-Visualisierung auf der rechten Seite (3D)
        qubit_title = Text("Qubits", font_size=30).move_to([4, 0, 0])
        self.add_fixed_in_frame_mobjects(qubit_title)
        self.play(Write(qubit_title))
        
        # Koordinatensystem erstellen
        axes = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=3,
            y_length=3,
            z_length=3
        ).shift(RIGHT * 4)
        self.add(axes)
        
        # Bloch-Kugel
        bloch_sphere = Sphere(radius=1, resolution=(20, 20))
        bloch_sphere.set_color(BLUE)
        bloch_sphere.set_opacity(0.2)
        bloch_sphere.move_to(axes.get_origin())
        self.add(bloch_sphere)
        
        # Zustandsbeschriftungen
        state_0 = Text("|0⟩", color=RED).scale(0.7).move_to(axes.c2p(0, 0, -1.5))
        state_1 = Text("|1⟩", color=GREEN).scale(0.7).move_to(axes.c2p(0, 0, 1.5))
        self.add_fixed_in_frame_mobjects(state_0, state_1)
        
        # Pfeil (Zustandsvektor)
        arrow = Arrow3D(
            start=axes.get_origin(),
            end=axes.get_origin() + [0, 0, 1],
            color=YELLOW,
            thickness=0.05
        )
        self.add(arrow)
        
        # Superposition-Text
        qubit_arrow = Arrow(start=[4, -2, 0], end=[4, -2.5, 0])
        qubit_state = Text("Superposition", font_size=24).move_to([4, -3, 0])
        self.add_fixed_in_frame_mobjects(qubit_arrow, qubit_state)
        self.play(Create(qubit_arrow), Write(qubit_state))
        
        # Animation des Pfeils mit mehr Bewegung nach unten
        def update_arrow(mob, dt):
            t = self.renderer.time % 4
            # Komplexere Bewegung mit mehr Betonung nach unten
            theta = t * TAU  # Volle Drehung in der XY-Ebene
            
            # Oszillation mit Bias nach unten
            phi = np.sin(t * PI) * PI/2 - PI/4
            
            x = np.sin(phi) * np.cos(theta)
            y = np.sin(phi) * np.sin(theta)
            z = np.cos(phi)
            
            new_end = axes.get_origin() + [x, y, z]
            mob.become(Arrow3D(start=axes.get_origin(), end=new_end, color=YELLOW, thickness=0.05))
        
        arrow.add_updater(update_arrow)
        
        self.wait(8)  # 8 Sekunden Animation zeigen

from manim import *
import numpy as np

class ZahlenDarstellung(Scene):
    def construct(self):
        # Titel und Unterstrich
        title = Text("Aufbau", font_size=48).to_edge(UP, buff=0.3)
        underline = Line(title.get_left(), title.get_right(), color=WHITE)
        underline.next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline))
        
        # Überschriften für die Tabelle
        computer_heading = Text("Computer", font_size=36).move_to([-3, 2, 0])
        quantum_heading = Text("Quantencomputer", font_size=36).move_to([3, 2, 0])
        
        self.play(
            Write(computer_heading),
            Write(quantum_heading)
        )
        
        # Tabelle erstellen
        table = MathTable(
            [
                ["n", "\\text{Bits}", "\\text{Qubits}"],
                ["1", "2^1 = 2 \\text{ Zahlen}", "2^1 = 2 \\text{ Zahlen in Superposition}"],
                ["2", "2^2 = 4 \\text{ Zahlen}", "2^2 = 4 \\text{ Zahlen in Superposition}"],
                ["3", "2^3 = 8 \\text{ Zahlen}", "2^3 = 8 \\text{ Zahlen in Superposition}"],
                ["10", "2^{10} = 1024 \\text{ Zahlen}", "2^{10} = 1024 \\text{ Zahlen in Superposition}"],
                ["n", "2^n \\text{ Zahlen}", "2^n \\text{ Zahlen in Superposition}"]
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1}
        ).scale(0.65).move_to([0, -0.3, 0])
        
        # Farbliche Hervorhebung
        table.add_highlighted_cell((1,1), color=BLUE_E)
        table.add_highlighted_cell((1,2), color=RED_E)
        table.add_highlighted_cell((1,3), color=GREEN_E)
        
        # Beispieleinträge für besseres Verständnis
        beispiel = MathTable(
            [
                ["n=1", "\\{0,1\\}", "\\{0,1\\} \\text{ gleichzeitig}"],
                ["n=2", "\\{00,01,10,11\\}", "\\{00,01,10,11\\} \\text{ gleichzeitig}"]
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1}
        ).scale(0.55).next_to(table, DOWN, buff=0.4)
        
        self.play(Create(table))
        self.play(Create(beispiel))
        
        # Mathematische Schlussfolgerung
        schlussfolgerung_titel = Text("Schlussfolgerung:", font_size=32).next_to(beispiel, DOWN, buff=0.4)
        
        schlussfolgerung = VGroup(
            MathTex(r"\text{Klassisch: } 2^n \text{ mögliche Zahlen - nur eine zur Zeit (linear)}", font_size=28),
            MathTex(r"\text{Quanten: } 2^n \text{ mögliche Zahlen - alle gleichzeitig (exponentiell)}", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(schlussfolgerung_titel, DOWN, buff=0.2)
        
        self.play(Write(schlussfolgerung_titel))
        self.play(Write(schlussfolgerung))
        
        self.wait(2)

from manim import *

class GateComparison(Scene):
    def construct(self):
        # Logisches UND-Gatter
        and_gate = VGroup()
        body = Polygon([-1, 1, 0], [1, 1, 0], [1, -1, 0], [-1, -1, 0])
        arc = Arc(start_angle=-PI/2, angle=PI, radius=1)
        arc.shift(RIGHT)
        input1 = Line([-2, 0.5, 0], [-1, 0.5, 0])
        input2 = Line([-2, -0.5, 0], [-1, -0.5, 0])
        output = Line([2, 0, 0], [3, 0, 0])
        and_gate.add(body, arc, input1, input2, output)
        
        and_label = Text("AND", font_size=36).move_to(body)
        and_gate.add(and_label)

        self.play(Create(and_gate))
        self.wait(2)

        # Beispiele für AND-Gatter
        example1 = VGroup(
            Text("0", font_size=24).next_to(input1, LEFT),
            Text("0", font_size=24).next_to(input2, LEFT),
            Text("0", font_size=24).next_to(output, RIGHT)
        )
        self.play(Write(example1))
        self.wait(1)
        self.play(FadeOut(example1))

        example2 = VGroup(
            Text("1", font_size=24).next_to(input1, LEFT),
            Text("1", font_size=24).next_to(input2, LEFT),
            Text("1", font_size=24).next_to(output, RIGHT)
        )
        self.play(Write(example2))
        self.wait(1)
        self.play(FadeOut(example2), FadeOut(and_gate))

        # Überschriften
        title = Text("Aufbau", font_size=48).to_edge(UP)
        underline = Line(title.get_left(), title.get_right(), color=WHITE)
        underline.next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline))

        computer_heading = Text("Computer", font_size=36).move_to([-3, 2, 0])
        quantum_heading = Text("Quantencomputer", font_size=36).move_to([3, 2, 0])
        self.play(Write(computer_heading), Write(quantum_heading))

        # Gatter-Typen für klassische Computer
        classical_gates = VGroup(
            Text("• AND", font_size=24),
            Text("• OR", font_size=24),
            Text("• NOT", font_size=24),
            Text("• XOR", font_size=24),
            Text("• NAND", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(computer_heading, DOWN, buff=0.5)

        # Gatter-Typen für Quantencomputer
        quantum_gates = VGroup(
            Text("• Hadamard", font_size=24),
            Text("• Pauli-X, Y, Z", font_size=24),
            Text("• CNOT", font_size=24),
            Text("• Toffoli", font_size=24),
            Text("• Rotation", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(quantum_heading, DOWN, buff=0.5)

        self.play(Write(classical_gates), Write(quantum_gates))
        self.wait(3)



from manim import *
import numpy as np

class FunctionalityComparison(Scene):
    def construct(self):
        # Titel und Unterstrich
        title = Text("Aufbau", font_size=48).to_edge(UP, buff=0.3)
        underline = Line(title.get_left(), title.get_right(), color=WHITE)
        underline.next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline))
        
        # Überschriften für Computer und Quantencomputer
        computer_heading = Text("Computer", font_size=36).move_to([-3, 2, 0])
        quantum_heading = Text("Quantencomputer", font_size=36).move_to([3, 2, 0])
        self.play(Write(computer_heading), Write(quantum_heading))
        
        # Binärdarstellung für Computer (links)
        binary_classical = VGroup(
            MathTex("0\\ 0 = 0"),
            MathTex("0\\ 1 = 1"),
            MathTex("1\\ 0 = 2"),
            MathTex("1\\ 1 = 3")
        ).arrange(DOWN, aligned_edge=LEFT).next_to(computer_heading, DOWN, buff=0.5)
        
        for bit in binary_classical:
            self.play(Write(bit))
        # Warten, bis die Darstellung auf der linken Seite fertig ist
        self.wait(1)
        
        # Binärdarstellung für Quantencomputer (rechts) erscheint erst danach
        binary_quantum = VGroup(
            MathTex("0\\ 0 = 0"),
            MathTex("0\\ 1 = 1"),
            MathTex("1\\ 0 = 2"),
            MathTex("1\\ 1 = 3")
        ).arrange(DOWN, aligned_edge=LEFT).next_to(quantum_heading, DOWN, buff=0.5)
        
        for qb in binary_quantum:
            self.play(Write(qb))
        
        self.wait(2)
        
        # Text "seriell" unter der Computer-Seite und "parallel" unter der Quantencomputer-Seite
        serial_text = Text("seriell", font_size=30).next_to(binary_classical, DOWN, buff=0.5)
        parallel_text = Text("parallel", font_size=30).next_to(binary_quantum, DOWN, buff=0.5)
        self.play(Write(serial_text), Write(parallel_text))
        
        # Berechnungsbeispiele:
        serial_calc = MathTex("7^2 = 49").next_to(serial_text, DOWN, buff=0.5)
        # Zerlege die parallele Rechnung in Einzelelemente, um einzelne Bestandteile gezielt bearbeiten zu können
        parallel_eq = MathTex(
            r"|7^0\rangle", "+", r"|7^1\rangle", "+", r"|7^2\rangle", "+", r"|7^3\rangle",
            "=",
            r"|1\rangle", "+", r"|7\rangle", "+", r"|49\rangle", "+", r"|343\rangle"
        ).scale(0.7).next_to(parallel_text, DOWN, buff=0.5)
        
        self.play(Write(serial_calc), Write(parallel_eq))
        self.wait(2)
        
        # Erzeuge Strichlinien, die über die Bestandteile gelegt werden, die gestrichen werden sollen.
        # In diesem Fall: |1⟩, |7⟩ und |343⟩. (Die Indizes entsprechend der Zerlegung:
        # 0: |7^0⟩, 1: +, 2: |7^1⟩, 3: +, 4: |7^2⟩, 5: +, 6: |7^3⟩, 7: =,
        # 8: |1⟩, 9: +, 10: |7⟩, 11: +, 12: |49⟩, 13: +, 14: |343⟩)
        strike_indices = [8, 10, 14]
        strike_lines = VGroup()
        for index in strike_indices:
            part = parallel_eq[index]
            start = part.get_left() - 0.1 * RIGHT
            end = part.get_right() + 0.1 * RIGHT
            # Zeichne eine Linie, die das Element horizontal durchstreicht.
            line = Line(start, end, color=RED)
            line.shift((part.get_center()[1] - line.get_center()[1]) * UP)
            strike_lines.add(line)
        
        self.play(Create(strike_lines))
        self.wait(2)
        
        # Alles ausblenden
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Exponentielle Steigerung von Qubits: Schrittweise Einblendung, wobei nur Zahlen (und falls nötig Details) erscheinen
        states_data = [
            (r"2^3 = 8", r"(000, 001, 010, 011,\\ 100, 101, 110, 111)"),
            (r"2^4 = 16", ""),
            (r"2^{20} = 1.048.576", ""),
            (r"2^{300} \approx 10^{90}", r"")
        ]
        
        for i, (expr, details) in enumerate(states_data):
            expr_tex = MathTex(expr, font_size=36)
            expr_tex.to_edge(UP, buff=2)
            expr_tex.shift(DOWN * (i * 1.0))
            self.play(Write(expr_tex))
            if details != "":
                # Bei mehrzeiligen Details verwenden wir Tex; '\\\\' sorgt für einen Zeilenumbruch.
                details_tex = Tex(details, font_size=24)
                details_tex.next_to(expr_tex, RIGHT, buff=0.5)
                self.play(Write(details_tex))
            self.wait(0.5)
        
        # Prominente Anzeige der Formel 2^n
        formula = MathTex("2^n", font_size=72).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(3)


from manim import *
import numpy as np

class QuantumVsClassicalMaze(Scene):
    def construct(self):
        # Define maze structure (0 = path, 1 = wall)
        maze_grid = np.array([
            [1,1,1,1,1,1,1,1],
            [1,0,0,0,1,0,0,1],
            [1,1,1,0,1,0,1,1],
            [1,0,1,0,0,0,0,1],
            [1,0,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1]
        ])
        
        # Create maze visualization
        maze = VGroup()
        cell_size = 0.6
        for i in range(maze_grid.shape[0]):
            for j in range(maze_grid.shape[1]):
                cell = Square(side_length=cell_size, fill_color=BLUE if maze_grid[i,j] else WHITE,
                             fill_opacity=1, stroke_width=2)
                cell.move_to([j*cell_size - 3, i*cell_size - 2, 0])
                maze.add(cell)
                
        start = Dot(color=GREEN).move_to(maze[8].get_center())
        end = Dot(color=RED).move_to(maze[40].get_center())
        
        # Set up titles
        title = Text("Maze Solving: Quantum vs Classical").to_edge(UP)
        classical_title = Text("Classical Computer\n(Serial Search)", font_size=24).to_edge(LEFT)
        quantum_title = Text("Quantum Computer\n(Parallel Search)", font_size=24).to_edge(RIGHT)
        
        # Create path trackers
        classical_path = VGroup()
        quantum_paths = VGroup()
        
        self.play(Create(maze), FadeIn(start), FadeIn(end), Write(title))
        self.wait(1)
        
        # Animate classical search
        classical_runner = Dot(color=RED).move_to(start.get_center())
        self.play(
            maze.animate.shift(LEFT*3.5),
            start.animate.shift(LEFT*3.5),
            end.animate.shift(LEFT*3.5),
            FadeIn(classical_title)
        )
        
        # Classical pathfinding algorithm (depth-first search visualization)
        classical_paths = [
            [8,9,10,18,26,25,24,32,40],       # Correct path
            [8,9,1],                          # Dead end 1
            [8,16,24,25,17,9,10,18,26,25,24,32,40],  # Backtracking
        ]
        
        for path in classical_paths:
            for idx in path:
                new_segment = Line(classical_runner.get_center(), maze[idx].get_center(), color=RED)
                classical_path.add(new_segment)
                self.play(
                    classical_runner.animate.move_to(maze[idx].get_center()),
                    Create(new_segment),
                    run_time=0.3
                )
            self.play(classical_runner.animate.move_to(start.get_center()), run_time=0.5)
        
        # Animate quantum search
        self.play(
            maze.animate.shift(RIGHT*7),
            start.animate.shift(RIGHT*7),
            end.animate.shift(RIGHT*7),
            FadeIn(quantum_title)
        )
        
        # Quantum parallel paths visualization
        all_quantum_paths = [
            [8,9,10,18,26,25,24,32,40],   # Correct path
            [8,9,1],                      # Dead end
            [8,16,24,32,40],              # Alternative path
            [8,16,24,25,17,9,10,18,26,25,24,32,40]
        ]
        
        quantum_runners = [
            Dot(color=BLUE).move_to(start.get_center()) 
            for _ in all_quantum_paths
        ]
        
        for path, runner in zip(all_quantum_paths, quantum_runners):
            q_path = VGroup()
            for idx in path:
                new_segment = Line(runner.get_center(), maze[idx].get_center(), color=BLUE)
                q_path.add(new_segment)
                self.play(
                    runner.animate.move_to(maze[idx].get_center()),
                    Create(new_segment),
                    run_time=0.5,
                    rate_func=linear
                )
            quantum_paths.add(q_path)
        
        # Final comparison
        self.play(
            maze.animate.move_to(ORIGIN).scale(0.7),
            start.animate.move_to(maze[8].get_center()),
            end.animate.move_to(maze[40].get_center()),
            classical_path.animate.set_color(RED).scale(0.7).shift(LEFT*2),
            quantum_paths.animate.set_color(BLUE).scale(0.7).shift(RIGHT*2),
            FadeOut(title),
            FadeOut(classical_title),
            FadeOut(quantum_title),
            run_time=2
        )
        
        comparison_text = Text("Quantum exploration completes\nall paths simultaneously", 
                             font_size=24).to_edge(DOWN)
        self.play(Write(comparison_text))
        self.wait(3)

from manim import *
import random
from manim import *
#from qiskit import QuantumCircuit, Aer, execute
import numpy as np

class QuantumMaze(ThreeDScene):
    def construct(self):
        # Maze configuration
        maze_size = 15
        cell_size = 0.5
        maze = self.generate_maze(maze_size, cell_size)
        
        # Animate maze creation
        self.play(Write(maze), run_time=2)
        self.wait(1)

        # Classical pathfinding
        classical_path = self.classical_solver(maze)
        self.play(Create(classical_path), run_time=5)
        self.wait(1)

        # Quantum pathfinding
        quantum_paths = self.quantum_solver(maze)
        self.play(Create(quantum_paths), run_time=3)
        self.wait(2)

    def generate_maze(self, size, cell_size):
        # Enhanced maze with more false paths using modified Growing Tree algorithm[3]
        grid = []
        for x in range(size):
            row = []
            for y in range(size):
                cell = Square(cell_size).set_fill(BLUE_E, 0.5)
                cell.move_to([x*cell_size, y*cell_size, 0])
                row.append(cell)
            grid.append(row)
        
        # Create false paths using probabilistic wall removal[6]
        for _ in range(int(size**2 * 0.3)):
            x, y = np.random.randint(1, size-1, 2)
            grid[x][y].set_fill(WHITE, 1)
        
        return VGroup(*[cell for row in grid for cell in row])

    def classical_solver(self, maze):
        # Depth-first search with backtrack visualization[2][4]
        path = VMobject(color=GREEN, stroke_width=8)
        steps = self.dfs_path(maze, (0,0), (maze_size-1,maze_size-1))
        path.set_points_as_corners([maze[x][y].get_center() for x,y in steps])
        return path

    def quantum_solver(self, maze):
        # Quantum path superposition using Grover's algorithm[10]
        qc = QuantumCircuit(4, 4)
        qc.h(range(4))
        qc.barrier()
        
        # Oracle for valid paths[9]
        qc.append(self.create_oracle(maze), range(4))
        
        # Grover diffusion
        qc.h(range(4))
        qc.z(range(4))
        qc.cz(0,3)
        qc.h(range(4))
        
        # Simulate quantum paths
        simulator = Aer.get_backend('statevector_simulator')
        result = execute(qc, simulator).result()
        statevector = result.get_statevector()
        
        # Visualize superposition paths
        paths = VGroup()
        for i, amp in enumerate(statevector):
            if abs(amp) > 0.1:
                path = self.decode_path(i)
                path_viz = VMobject(color=RED, stroke_width=4)
                path_viz.set_points_as_corners(
                    [maze[x][y].get_center() for x,y in path]
                )
                paths.add(path_viz)
        
        return paths

    def create_oracle(self, maze):
        # Simplified path validity checker[8]
        oracle = QuantumCircuit(4)
        # ... (complex gate sequence validating maze paths)
        return oracle

    def dfs_path(self, maze, start, end):
        # Traditional DFS implementation[4]
        stack = [start]
        visited = set()
        path = []
        
        while stack:
            x,y = stack.pop()
            path.append((x,y))
            if (x,y) == end:
                return path
            # Neighbor exploration logic
            # ...
        
        return path


from manim import *
import random
import numpy as np

class MazeComparison(Scene):
    def construct(self):
# PARAMETERS
        maze_size = 11 # Must be an odd number for our generation algorithm
        cell_size = 0.7 # Visual size of each cell (square)
        extra_opening_prob = 0.1 # Chance to add extra openings (false paths)

        # Generate a perfect maze using recursive backtracking.
        maze = self.generate_maze(maze_size)
        # Add extra openings so that there are more false paths.
        self.add_false_paths(maze, extra_opening_prob)
        # Guarantee that start and end cells are open.
        maze = 1
        maze[maze_size - 2][maze_size - 2] = 1

        # Create and display the maze visualization.
        # (Cells painted WHITE for passages and DARK_GRAY for walls)
        maze_vgroup = self.create_maze_visual(maze, cell_size)
        # Position the maze to the left so that we have room to show the “quantum” results later.
        maze_vgroup.shift(LEFT * 5)
        self.play(FadeIn(maze_vgroup))
        self.wait(1)

        # CLASSICAL SOLVER (Computer)
        start = (1, 1)
        end = (maze_size - 2, maze_size - 2)
        classical_explored, classical_solution = self.solve_maze_classical(maze, start, end)

        # Animate the classical search.
        # A blue dot will travel along the order in which cells were visited.
        dot_classical = Dot(point=self.cell_center(start, cell_size), color=BLUE)
        label_classical = Text("Computer", font_size=24).next_to(dot_classical, UP)
        self.add(dot_classical, label_classical)
        for pos in classical_explored:
            target = self.cell_center(pos, cell_size)
            self.play(dot_classical.animate.move_to(target), run_time=0.15)
        self.wait(0.5)

        # Now highlight the final solution path (green line).
        classical_path_points = [self.cell_center(pos, cell_size) for pos in classical_solution]
        classical_line = VMobject(color=GREEN, stroke_width=6)
        classical_line.set_points_as_corners(classical_path_points)
        self.play(Create(classical_line), run_time=2)
        self.wait(1)
        self.remove(dot_classical, label_classical)
        self.wait(1)

        # QUANTUM SOLVER (Quantumcomputer)
        # We “simulate” a quantum algorithm by finding several different solution paths
        # (i.e. going all possible paths at once).
        quantum_paths = self.solve_maze_quantum(maze, start, end, max_paths=4)
        quantum_group = VGroup(*quantum_paths)
        # Position the quantum solutions on the right.
        quantum_group.shift(RIGHT * 5)
        label_quantum = Text("Quantumcomputer", font_size=24).next_to(quantum_group, UP)
        self.play(FadeIn(label_quantum))
        self.play(Create(quantum_group), run_time=3)
        self.wait(2)

    def generate_maze(self, size):
        """
        Generate a perfect maze (without any cycles) using recursive backtracking.
        The maze is represented as a 2D list.
        0 = wall; 1 = open passage.
        """
        maze = [[0 for _ in range(size)] for _ in range(size)]

        def in_bounds(x, y):
            return 0 <= x < size and 0 <= y < size

        def carve(x, y):
            maze[x][y] = 1  # Mark current cell as a passage.
            # Consider neighbors two cells away (N, S, E, W)
            directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if in_bounds(nx, ny) and maze[nx][ny] == 0:
                    # Also open the wall between the current cell and the neighbor.
                    wall_x, wall_y = x + dx // 2, y + dy // 2
                    maze[wall_x][wall_y] = 1
                    carve(nx, ny)
        # Start carving from cell (1,1)
        carve(1, 1)
        return maze

    def add_false_paths(self, maze, probability):
        """
        Open additional walls randomly so that extra false paths exist.
        """
        size = len(maze)
        for x in range(1, size - 1):
            for y in range(1, size - 1):
                if maze[x][y] == 0:
                    # If at least one of the four neighbors is already a passage, sometimes open this wall.
                    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                    for nx, ny in neighbors:
                        if maze[nx][ny] == 1:
                            if random.random() < probability:
                                maze[x][y] = 1
                                break

    def create_maze_visual(self, maze, cell_size):
        """
        Create a VGroup where each maze cell is drawn as a square.
        Walls are DARK_GRAY and passages are WHITE.
        """
        size = len(maze)
        group = VGroup()
        for i in range(size):
            for j in range(size):
                # Choose the color for the cell.
                if maze[i][j] == 0:
                    color = DARK_GRAY
                else:
                    color = WHITE
                square = Square(side_length=cell_size,
                                fill_color=color,
                                fill_opacity=1,
                                stroke_color=BLACK)
                # Place cell: use (j, -i) so that increasing row goes downward.
                square.move_to(np.array([j * cell_size, -i * cell_size, 0]))
                group.add(square)
        return group

    def cell_center(self, pos, cell_size):
        """
        Convert a maze grid coordinate pos=(row, col) into a point (in scene coordinates)
        corresponding to the center of that cell.
        """
        row, col = pos
        return np.array([col * cell_size, -row * cell_size, 0])

    def solve_maze_classical(self, maze, start, end):
        """
        Solve the maze using a depth-first search.
        Return a tuple:
        - explored_order: the order in which cells were first visited (for animation)
        - solution_path: the final path from start to end.
        """
        size = len(maze)
        stack = [start]
        came_from = {start: None}
        explored_order = [start]

        def neighbors(pos):
            x, y = pos
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] == 1:
                    yield (nx, ny)

        found = False
        while stack:
            current = stack.pop()
            if current == end:
                found = True
                break
            for nbr in neighbors(current):
                if nbr not in came_from:
                    came_from[nbr] = current
                    stack.append(nbr)
                    explored_order.append(nbr)
        # Reconstruct the solution path from end to start.
        path = []
        if found:
            current = end
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
        return explored_order, path

    def solve_maze_quantum(self, maze, start, end, max_paths=4):
        """
        Simulate a “quantum” solver by using DFS to collect several (up to max_paths)
        different simple paths from start to end. (In a true quantum algorithm, all paths
        would be explored simultaneously.) Each solution will be drawn as a colored line.
        """
        size = len(maze)
        solutions = []

        def dfs(current, path, visited):
            if current == end:
                solutions.append(path.copy())
                return
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = current + dx, current + dy
                next_cell = (nx, ny)
                if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] == 1 and next_cell not in visited:
                    visited.add(next_cell)
                    path.append(next_cell)
                    dfs(next_cell, path, visited)
                    path.pop()
                    visited.remove(next_cell)
                    if len(solutions) >= max_paths:
                        return

        dfs(start, [start], {start})

        # Create a list of VMobjects – one for each solution path.
        paths_vobjects = []
        colors = [RED, ORANGE, PINK, YELLOW]
        for i, sol in enumerate(solutions):
            points = [self.cell_center(pos, 0.7) for pos in sol]
            line = VMobject(stroke_width=4)
            line.set_points_as_corners(points)
            line.set_color(colors[i % len(colors)])
            paths_vobjects.append(line)
        return paths_vobjects


from manim import *
import random

class MazeWithFalsePaths(Scene):
    def construct(self):
        # Maze configuration
        size = 21  # Must be an odd number to ensure proper cell/wall layout
        cell_size = 0.35
        base_color = BLUE_E   # Color for walls
        path_color = GOLD     # Color for passages (including false paths)
        accent_color = PURPLE # Accent color for final effects
        false_path_prob = 0.15  # Chance to remove an extra wall for a false path

        # Create a 2D grid of squares to represent cells/walls
        grid = [[Square(cell_size, color=base_color, fill_opacity=1)
                 for _ in range(size)]
                for _ in range(size)]
        # Arrange the cells into a grid and center it
        group = VGroup(*[cell for row in grid for cell in row]).arrange_in_grid(
            rows=size, cols=size, buff=0)
        group.center()

        # Draw maze borders around the entire grid
        borders = SurroundingRectangle(group, buff=0, color=WHITE, stroke_width=12)
        self.add(borders)

        # Prepare visited matrix and stack for DFS maze generation
        visited = [[False for _ in range(size)] for _ in range(size)]
        stack = []

        # Start the DFS from cell (1,1) which represents a passage
        start = (1, 1)
        stack.append(start)
        visited[start[0]][start[1]] = True

        # Generate a "perfect" maze (one unique solution) with DFS;
        # passages are created by “removing” walls between cells.
        while stack:
            x, y = stack[-1]
            neighbors = []
            # Look for neighbors two cells away (this leaves a wall cell in between)
            for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                nx, ny = x + dx, y + dy
                if 0 < nx < size - 1 and 0 < ny < size - 1 and not visited[nx][ny]:
                    neighbors.append((nx, ny))
            if neighbors:
                nx, ny = random.choice(neighbors)
                # Determine the wall cell between current cell (x,y) and neighbor (nx,ny)
                wx, wy = (x + nx) // 2, (y + ny) // 2

                # Animate the removal of the wall by changing colors and opacities.
                self.play(
                    grid[nx][ny].animate.set_color(path_color).set_fill_opacity(0.7),
                    grid[wx][wy].animate.set_color(path_color).set_fill_opacity(0.7),
                    run_time=0.08,
                    rate_func=smooth
                )
                visited[nx][ny] = True
                stack.append((nx, ny))
            else:
                stack.pop()

        # The maze generated above is "perfect" (one solution with no loops).
        # Now, to add more false paths, iterate over potential wall cells and remove
        # some extra walls that separate already connected passages.
        false_path_anims = []
        for i in range(1, size - 1):
            for j in range(1, size - 1):
                # Only consider cells which are still walls (have the base color)
                if grid[i][j].get_color() == base_color:
                    # Horizontal candidates: cell lies between two passages
                    if i % 2 == 1 and j % 2 == 0:
                        left_color = grid[i][j - 1].get_color()
                        right_color = grid[i][j + 1].get_color()
                        if left_color == path_color and right_color == path_color:
                            if random.random() < false_path_prob:
                                false_path_anims.append(
                                    grid[i][j].animate.set_color(path_color).set_fill_opacity(0.7)
                                )
                    # Vertical candidates: similar idea for vertical walls.
                    elif j % 2 == 1 and i % 2 == 0:
                        up_color = grid[i - 1][j].get_color()
                        down_color = grid[i + 1][j].get_color()
                        if up_color == path_color and down_color == path_color:
                            if random.random() < false_path_prob:
                                false_path_anims.append(
                                    grid[i][j].animate.set_color(path_color).set_fill_opacity(0.7)
                                )
        if false_path_anims:
            self.play(*false_path_anims, run_time=1, rate_func=smooth)

        # Final visual flourish: apply a gradient effect to the maze and emphasize an exit.
        self.play(
            group.animate.set_color_by_gradient(path_color, accent_color),
            borders.animate.set_color_by_gradient(accent_color, path_color),
            run_time=2
        )

        # Place an accent dot at the maze exit (using cell at bottom-right)
        exit_dot = Dot(point=grid[size - 2][size - 2].get_center(), color=accent_color, radius=0.18)
        self.play(FadeIn(exit_dot, scale=0.5), run_time=1)
        self.wait(2)

#!/usr/bin/env python3
from manim import *
import random
from collections import deque

class MazeWithFalsePathsAndSolution(Scene):
    def construct(self):
        # CONFIGURATION
        size = 21            # Must be odd for proper maze cell & wall layout.
        cell_size = 0.35
        base_color = BLUE_E  # Initial wall color.
        path_color = GOLD    # Color for passages.
        accent_color = PURPLE  # Accent color used for gradients and the solution path.
        false_path_prob = 0.15  # Chance for an extra wall removal to create a false path.

        # CREATE THE GRID
        grid = [[Square(side_length=cell_size, color=base_color, fill_opacity=1)
                 for _ in range(size)]
                for _ in range(size)]
        group = VGroup(*[grid[i][j] for i in range(size) for j in range(size)])
        group.arrange_in_grid(rows=size, cols=size, buff=0)
        group.center()

        # Draw a solid border around the maze.
        borders = SurroundingRectangle(group, buff=0, color=WHITE, stroke_width=12)
        self.add(borders)

        # INITIALIZE MAZE DATA STRUCTURES
        # maze_map is a 2D boolean grid where True indicates an open path.
        maze_map = [[False for _ in range(size)] for _ in range(size)]
        # visited helps track which cells have been opened.
        visited = [[False for _ in range(size)] for _ in range(size)]
        stack = []

        # Start DFS maze generation at cell (1,1)
        start = (1, 1)
        stack.append(start)
        visited[start[0]][start[1]] = True
        maze_map[start[0]][start[1]] = True

        # Open the starting cell visually.
        self.play(
            grid[start[0]][start[1]].animate.set_color(path_color).set_fill_opacity(0.7),
            run_time=0.1
        )

        # DFS MAZE GENERATION (Perfect Maze)
        while stack:
            x, y = stack[-1]
            neighbors = []
            # Look in four directions two cells away (leaving a wall cell in between).
            for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                nx, ny = x + dx, y + dy
                if 0 < nx < size - 1 and 0 < ny < size - 1 and not visited[nx][ny]:
                    neighbors.append((nx, ny))
            if neighbors:
                nx, ny = random.choice(neighbors)
                wx, wy = (x + nx) // 2, (y + ny) // 2  # wall cell between current and neighbor

                # Animate the removal of the wall between cells.
                self.play(
                    grid[nx][ny].animate.set_color(path_color).set_fill_opacity(0.7),
                    grid[wx][wy].animate.set_color(path_color).set_fill_opacity(0.7),
                    run_time=0.08, rate_func=smooth
                )
                visited[nx][ny] = True
                maze_map[nx][ny] = True
                maze_map[wx][wy] = True
                stack.append((nx, ny))
            else:
                stack.pop()

        # ADD FALSE PATHS (Extra open passages to create loops)
        false_path_anims = []
        for i in range(1, size - 1):
            for j in range(1, size - 1):
                if not maze_map[i][j]:
                    # For horizontal walls: check if cells to the left and right are open.
                    if i % 2 == 1 and j % 2 == 0:
                        if maze_map[i][j - 1] and maze_map[i][j + 1]:
                            if random.random() < false_path_prob:
                                false_path_anims.append(
                                    grid[i][j].animate.set_color(path_color).set_fill_opacity(0.7)
                                )
                                maze_map[i][j] = True
                    # For vertical walls: check for open cells above and below.
                    elif j % 2 == 1 and i % 2 == 0:
                        if maze_map[i - 1][j] and maze_map[i + 1][j]:
                            if random.random() < false_path_prob:
                                false_path_anims.append(
                                    grid[i][j].animate.set_color(path_color).set_fill_opacity(0.7)
                                )
                                maze_map[i][j] = True
        if false_path_anims:
            self.play(*false_path_anims, run_time=1, rate_func=smooth)

        # FINAL AESTHETICS: apply gradient effects.
        self.play(
            group.animate.set_color_by_gradient(path_color, accent_color),
            borders.animate.set_color_by_gradient(accent_color, path_color),
            run_time=2
        )

        # SOLVE THE MAZE WITH BFS (Breadth-First Search)
        def bfs(maze, start, end):
            queue = deque()
            queue.append(start)
            parents = {start: None}
            while queue:
                current = queue.popleft()
                if current == end:
                    break
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = current[0] + dx, current[1] + dy
                    if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] and (nx, ny) not in parents:
                        parents[(nx, ny)] = current
                        queue.append((nx, ny))
            path_ = []
            cell = end
            if cell not in parents:
                return []  # No solution found (should not occur)
            while cell is not None:
                path_.append(cell)
                cell = parents[cell]
            path_.reverse()
            return path_

        start_cell = (1, 1)
        end_cell = (size - 2, size - 2)
        solution = bfs(maze_map, start_cell, end_cell)

        if solution:
            # Convert maze cell indexes to positions.
            solution_points = [grid[i][j].get_center() for i, j in solution]
            solution_line = VMobject()
            solution_line.set_points_as_corners(solution_points)
            solution_line.set_color(accent_color)
            solution_line.set_stroke(width=6)
            self.play(Create(solution_line), run_time=3)
            
            # Add a dot that traverses the solution path.
            dot = Dot(color=accent_color, radius=0.15)
            self.add(dot)
            self.play(MoveAlongPath(dot, solution_line), run_time=3, rate_func=linear)
        else:
            print("No solution found!")

        # Mark the exit cell with an accent dot.
        exit_dot = Dot(point=grid[end_cell[0]][end_cell[1]].get_center(),
                       color=accent_color, radius=0.18)
        self.play(FadeIn(exit_dot, scale=0.5), run_time=1)
        self.wait(2)
from manim import *

class WillowExplanation(Scene):
    def construct(self):
        # Quote from Hartmut Neven
        quote = Text(
            "It lends credence to the notion that quantum computation occurs in many parallel universes, in line with the idea that we live in a multiverse",
            font_size=32, color=BLUE
        ).to_edge(UP)
        attribution = Text(
            "- Hartmut Neven, Google Quantum AI",
            font_size=24, color=GRAY
        ).next_to(quote, DOWN, buff=0.5)
        self.play(Write(quote), Write(attribution))
        self.wait(2)
        
        # Fade out the quote using FadeOut (instead of .fade(), which causes the error)
        self.play(FadeOut(quote, run_time=1.5), FadeOut(attribution, run_time=1.5))
        
        # Explain how Willow works
        
        # 1. Quantum parallelism: Superposition & Entanglement
        quantum_parallelism = Text(
            "Quantum Parallelism via Superposition & Entanglement",
            font_size=36, color=YELLOW
        ).to_edge(UP)
        self.play(Write(quantum_parallelism))
        
        # Create a qubit (circle) to represent a qubit in superposition
        qubit = Circle(radius=0.3, color=BLUE, fill_opacity=0.2)
        qubit.next_to(quantum_parallelism, DOWN, buff=1)
        self.play(Create(qubit))
        
        # Explain superposition with a text label
        superposition = Text(
            "Superposition: Qubits exist in multiple states simultaneously",
            font_size=24, color=RED
        ).next_to(qubit, DOWN, buff=0.5)
        self.play(Write(superposition))
        
        # Animate entanglement: show two entangled qubits connected by a line
        entangled_qubits = VGroup(
            Circle(radius=0.3, color=BLUE, fill_opacity=0.2),
            Circle(radius=0.3, color=BLUE, fill_opacity=0.2)
        ).arrange(RIGHT, buff=0.5).next_to(superposition, DOWN, buff=0.5)
        entanglement_line = Line(
            entangled_qubits[0].get_center(), entangled_qubits[1].get_center(), color=YELLOW
        )
        self.play(
            Create(entangled_qubits),
            Create(entanglement_line),
            Write(Text("Entanglement", font_size=24, color=YELLOW).next_to(entanglement_line, DOWN))
        )
        
        # 2. Explain the Random Circuit Sampling (RCS) Benchmark used in Willow
        rcs_explanation = Text(
            "Random Circuit Sampling (RCS) Benchmark",
            font_size=36, color=YELLOW
        ).to_edge(UP)
        self.play(
            FadeOut(quantum_parallelism),
            FadeOut(superposition),
            FadeOut(entangled_qubits),
            FadeOut(entanglement_line),
            Write(rcs_explanation)
        )
        
        # Show a fictitious time comparison between Willow and classical computers
        time_comparison = VGroup(
            Text("Willow: 5 Minutes", font_size=24, color=GREEN),
            Text("Classical Supercomputer: 10^25 Years", font_size=24, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(rcs_explanation, DOWN, buff=0.5)
        self.play(Write(time_comparison))
        
        # 3. Illustrate the Many-Worlds Interpretation (Parallel Universes)
        multiverse_text = Text(
            "Many-Worlds Interpretation of Quantum Mechanics",
            font_size=36, color=YELLOW
        ).to_edge(UP)
        self.play(
            FadeOut(rcs_explanation), 
            FadeOut(time_comparison), 
            Write(multiverse_text)
        )
        
        # Animate a simple "multiverse" (three dots representing parallel universes)
        multiverse_animation = VGroup(
            Dot(radius=0.1, color=BLUE).move_to([-2, 0, 0]),
            Dot(radius=0.1, color=BLUE).move_to([0, 0, 0]),
            Dot(radius=0.1, color=BLUE).move_to([2, 0, 0])
        )
        self.play(Create(multiverse_animation))
        self.wait(1)
        
        # Conclusion: Summarize the power of quantum parallelism
        conclusion = Text(
            "Quantum Computers leverage quantum parallelism,\nenabling calculations that appear to span multiple universes",
            font_size=28, color=YELLOW
        ).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(3)

from manim import *
import numpy as np
import random
from manim import *
import numpy as np
import random

from manim import *
import numpy as np
import random
from manim import *
import numpy as np
import random
class TSPComparison(Scene):
    def construct(self):
        # Set seeds for reproducibility
        np.random.seed(10)
        random.seed(10)
        title = Text("Problem des Handlungsreisenden", font_size=48).to_edge(UP, buff=0.3)
        underline = Line(title.get_left(), title.get_right(), color=WHITE)
        underline.next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline))

        # Define the start and end points (now the same)
        start_point = np.array([-4, 0, 0])  # Far left
        end_point = start_point  # Same as start point

        # Generate intermediate points randomly spread between start and end
        num_cities = 20
        intermediate_points = [
            np.array([random.uniform(-5.5, 5.5), random.uniform(-3, 3), 0])
            for _ in range(num_cities - 2)
        ]
        city_positions = [start_point] + intermediate_points + [end_point]

        # Create dots for each city; highlight start/end point
        city_dots = VGroup(*[Dot(point, radius=0.12, color=WHITE) for point in city_positions])
        city_dots[0].set_color(YELLOW)  # Start/end point
        city_dots[-1].set_color(YELLOW)  # Start/end point (duplicate)

        self.play(FadeIn(city_dots))
        start_label = Tex("Start/Ende", font_size=40).next_to(city_dots[0], LEFT)
        self.play(Write(start_label))
        self.wait(1)

        #############################
        ## CLASSICAL COMPUTER APPROACH
        #############################
        classical_title = Tex("Computer", font_size=40).next_to(start_label, UP, buff=0.3)
        self.play(Write(classical_title))
        self.wait(1)

        def route_distance(route):
            dist = 0
            for i in range(len(route) - 1):
                p1 = city_positions[route[i]]
                p2 = city_positions[route[i + 1]]
                dist += np.linalg.norm(p2 - p1)
            return dist

        classical_candidates = []
        num_classical_candidates = 5
        for _ in range(num_classical_candidates):
            candidate = [0] + random.sample(range(1, num_cities - 1), num_cities - 2) + [num_cities - 1]
            classical_candidates.append(candidate)

        distances = [route_distance(route) for route in classical_candidates]
        best_index = np.argmin(distances)
        optimal_candidate = classical_candidates[best_index]

        for idx, candidate in enumerate(classical_candidates):
            points = [city_positions[i] for i in candidate]
            line = VMobject()
            line.set_points_as_corners(points)
            line.set_stroke(color=RED, width=3)
            
            self.play(Create(line), run_time=1)
            self.wait(0.8)
            self.play(FadeOut(line), run_time=0.5)
            self.wait(0.2)
            
        optimal_points = [city_positions[i] for i in optimal_candidate]
        optimal_classical_line = VMobject()
        optimal_classical_line.set_points_as_corners(optimal_points)
        optimal_classical_line.set_stroke(color=GREEN, width=4)
        
        self.play(Create(optimal_classical_line), run_time=1)
        optimal_label = Tex("Optimaler Weg", font_size=40, color=GREEN).next_to(optimal_classical_line, DOWN)
        self.play(Write(optimal_label))
        self.wait(2)

        self.play(FadeOut(classical_title), FadeOut(optimal_label), FadeOut(optimal_classical_line))
        self.wait(1)

        #############################
        ## QUANTUM COMPUTER APPROACH
        #############################
        quantum_title = Tex("Quantencomputer", font_size=40).next_to(start_label, UP, buff=0.3)
        self.play(Write(quantum_title))
        self.wait(1)

        quantum_candidates = VGroup()
        num_quantum_candidates = 30
        quantum_routes = []
        
        for _ in range(num_quantum_candidates):
            candidate = [0] + random.sample(range(1, num_cities - 1), num_cities - 2) + [num_cities - 1]
            quantum_routes.append(candidate)
            
            points = [city_positions[i] for i in candidate]
            candidate_line = VMobject()
            candidate_line.set_points_as_corners(points)
            candidate_line.set_stroke(color=BLUE, width=2, opacity=0.2)
            quantum_candidates.add(candidate_line)
        
        self.play(FadeIn(quantum_candidates), run_time=1.5)
        self.wait(2)
        
        quantum_distances = [route_distance(route) for route in quantum_routes]
        quantum_best_index = np.argmin(quantum_distances)
        quantum_optimal = quantum_routes[quantum_best_index]
        
        optimal_points = [city_positions[i] for i in quantum_optimal]
        optimal_quantum_line = VMobject()
        optimal_quantum_line.set_points_as_corners(optimal_points)
        optimal_quantum_line.set_stroke(color=GREEN, width=5)
        
        self.play(Create(optimal_quantum_line), run_time=1.5)
        optimal_quantum_label = Tex("Optimaler Weg", font_size=40, color=GREEN).next_to(optimal_quantum_line, DOWN)
        self.play(Write(optimal_quantum_label))
        self.wait(2)
        
        
        self.play(
            FadeOut(quantum_title),
            FadeOut(quantum_candidates),
            FadeOut(optimal_quantum_line),
            FadeOut(optimal_quantum_label),
            FadeOut(city_dots),
            FadeOut(start_label)
        )
        self.wait(1)


from manim import *

class QuantumMultiverse(Scene):
    def construct(self):
        # Display the quote
        quote = Text(
            '"It lends credence to the notion that quantum computation\n'
            'occurs in many parallel universes, in line with the idea\n'
            'that we live in a multiverse"\n',
            font_size=20,
            color=YELLOW,
            font="Italic"
        ).scale(1.2).center()

        
        author = Text("- Hartmut Neven, Google Quantum AI Founder", font_size=20, color=GRAY).next_to(quote, DOWN, buff=0.5)
        
        self.play(Write(quote), Write(author))
        self.wait(3)
        
        # Fade out the quote
        self.play(FadeOut(quote), FadeOut(author))
        
        # Display the time comparison
        time_text = Text("10,000,000,000,000,000,000,000,000 Jahre", font_size=20, color=RED).scale(1.2).center()
        subtext = Text("Supercomputer vs. under five minutes for Google's quantum computer", font_size=24).next_to(time_text, DOWN, buff=0.5)
        
        self.play(FadeIn(time_text), FadeIn(subtext))
        self.wait(3)
        
        # Fade out everything
        self.play(FadeOut(time_text), FadeOut(subtext))
from manim import *
from manim import *
from manim import *

class IonTrapQuantumComputer(Scene):
    def construct(self):
        # Titel
        title = Text("Ionenfallen-Quantencomputer", font_size=48).to_edge(UP, buff=0.3)
        underline = Line(title.get_left(), title.get_right(), color=WHITE)
        underline.next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline))
        
        # Vakuumkammer
        chamber = Rectangle(height=4, width=6, color=BLUE).shift(DOWN)
        chamber_label = Text("Vakuumkammer", font_size=24).next_to(chamber, UP)
        self.play(Create(chamber), Write(chamber_label))
        
        # Paul-Falle
        trap = Rectangle(height=1, width=3, color=YELLOW).move_to(chamber.get_center())
        trap_label = Text("Paul-Falle", font_size=20).next_to(trap, UP, buff=0.1)
        self.play(Create(trap), Write(trap_label))
        
        # Ionen
        ions = VGroup(*[Dot(color=RED) for _ in range(5)]).arrange(RIGHT, buff=0.5).move_to(trap)
        ion_label = Text("Ionen (z.B. Ca-40, Yb-171)", font_size=20).next_to(ions, DOWN, buff=0.1)
        self.play(Create(ions), Write(ion_label))
        
        # Laser (jetzt nicht mehr auf der Vakuumkammer)
        laser1 = Arrow(start=chamber.get_top() + LEFT*2, end=ions[0].get_center(), color=GREEN)
        laser2 = Arrow(start=chamber.get_top() + RIGHT*2, end=ions[-1].get_center(), color=GREEN)
        laser_label = Text("Laser (729nm für Ca-40)", font_size=20).next_to(chamber, UP, buff=0.5)
        self.play(Create(laser1), Create(laser2), Write(laser_label))

        self.wait(2)

        # Alles ausblenden
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Neue Überschrift
        new_title = Text("Weitere Ansätze", font_size=48).to_edge(UP, buff=0.3)
        new_underline = Line(new_title.get_left(), new_title.get_right(), color=WHITE)
        new_underline.next_to(new_title, DOWN, buff=0.1)
        self.play(Write(new_title), Create(new_underline))

        # Liste der weiteren Ansätze
        approaches = VGroup(
            Text("• Supraleitende Qubits", font_size=40),
            Text("• Photonische Systeme", font_size=40),
            Text("• Spin-Qubits in Festkörpern", font_size=40),
            Text("• Neutrale Atome in optischen Gittern", font_size=40),
            Text("• Quantenpunkte in Halbleitern", font_size=40),
            Text("• Topologische Qubits", font_size=40)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(new_underline, DOWN, buff=0.5)

        for approach in approaches:
            self.play(Write(approach))
            self.wait(0.5)

        self.wait(2)

from manim import *

class Herausforderungen(Scene):
    def construct(self):
        # Titel
        title = Text("Herausforderungen", font_size=48).to_edge(UP, buff=0.3)
        underline = Line(title.get_left(), title.get_right(), color=WHITE)
        underline.next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline))
        
        # Stichpunkte
        points = VGroup(
            Text("• Dekohärenz & Instabilität", font_size=40),
            Text("• Fehleranfälligkeit", font_size=40),
            Text("• Skalierungsprobleme", font_size=40),
            Text("• Programmierung", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(underline, DOWN, buff=1.0)
        
        # Einblenden der Stichpunkte
        for point in points:
            self.play(Write(point))
            self.wait(0.5)
        
        self.wait(2)

from manim import *

class WillowErrorCorrection(Scene):
    def construct(self):
        # Titel
        title = Text("Fehlerkorrektur im Google Willow Chip", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Physische Qubits darstellen
        physical_qubits = VGroup(*[Circle(radius=0.2, color=BLUE) for _ in range(49)])
        physical_qubits.arrange_in_grid(7, 7, buff=0.3).shift(DOWN)
        self.play(Create(physical_qubits))

        # Logisches Qubit hervorheben
        logical_qubit = SurroundingRectangle(physical_qubits, buff=0.2, color=YELLOW)
        logical_label = Text("Logisches Qubit", font_size=24).next_to(logical_qubit, UP)
        self.play(Create(logical_qubit), Write(logical_label))

        # Fehler simulieren
        error = Cross(scale_factor=0.2, color=RED).move_to(physical_qubits[24])
        self.play(Create(error))

        # Fehlerkorrektur visualisieren
        correction_arrows = VGroup(*[
            Arrow(start=physical_qubits[i].get_center(), end=physical_qubits[24].get_center(), color=GREEN, buff=0.1)
            for i in [23, 25, 17, 31]
        ])
        self.play(Create(correction_arrows))

        # Fehler korrigieren
        self.play(FadeOut(error), Flash(physical_qubits[24], color=GREEN, flash_radius=0.3))

        self.wait(2)

from manim import *

class Anwendungen(Scene):
    def construct(self):
        # Titel
        title = Text("Anwendung", font_size=48).to_edge(UP, buff=0.3)
        underline = Line(title.get_left(), title.get_right(), color=WHITE)
        underline.next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline))
        
        # Stichpunkte
        points = VGroup(
            Text("• Materialforschung", font_size=40),
            Text("• Physikalische Simulation", font_size=40),
            Text("• Optimierungsprobleme in Logistik & Finanzen", font_size=40),
            Text("• KI & Maschinelles Lernen", font_size=40),
            Text("• Klimamodelle & Wetterprognosen", font_size=40),
            Text("• Kryptographie", font_size=40)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(underline, DOWN, buff=1.0)
        
        # Materialforschung und Vergleich
        self.play(Write(points[0]))
        
        comparison = VGroup(
            MathTex(r"\text{Computer: } 100 \text{ Atome} \Rightarrow 2^{100} \text{ Zustände}"),
            MathTex(r"\text{Quantencomputer: } 100 \text{ Atome} \Rightarrow 100 \text{ Zustände}")
        ).arrange(DOWN, buff=0.5).move_to(ORIGIN).next_to(points[0], DOWN, buff=0.5).center()
        
        self.play(Write(comparison))
        self.wait(2)
        
        # Ausblenden des Vergleichs
        self.play(FadeOut(comparison))
        
        # Restliche Stichpunkte einblenden
        for point in points[1:]:
            self.play(Write(point))
            self.wait(0.5)
        
        self.wait(2)

from manim import *
import math
from manim import *
from manim import *
import math

class RSABreakdown(Scene):
    def construct(self):
        # HTTPS und Sicherheitshinweis
        url = Text("https://www.google.com/", font_size=36)
        self.play(Write(url))
        s_indicator = Text("Sicherheit durch RSA-2048", font_size=24).next_to(url, DOWN)
        self.play(Write(s_indicator))
        self.wait(2)

        # RSA-Erklärung
        title = Text("RSA-2048: Mathematische Basis", font_size=36).to_edge(UP)
        self.play(ReplacementTransform(url, title))
        
        # Primzahlbeispiel (vereinfacht)
        primes = VGroup(
            MathTex("p = 10^{308}"),  # Typische Primzahlgröße für RSA-2048
            MathTex("q = 10^{308}"),
            MathTex("N = p \\cdot q = 10^{616}"),
        ).arrange(DOWN, buff=0.7)
        self.play(LaggedStart(*[Write(eq) for eq in primes], lag_ratio=0.7))
        self.wait(2)

        # GNFS-Zeitkomplexität
        complexity = MathTex(
            "\\text{Zeit} \\propto e^{1{,}92 \\cdot (\\ln N)^{1/3} \\cdot (\\ln \\ln N)^{2/3}}",
            font_size=30
        ).next_to(primes, DOWN)
        
        self.play(Write(complexity))
        self.wait(1)

        # Supercomputer-Zeit
        time_classical = Text("4,28 Mrd. Jahre\n(mit 10^18 Operationen/s)", font_size=24, color=RED)
        time_quantum = Text("100 Sekunden\n(mit 20 Mio. Qubits)", font_size=24, color=GREEN)
        
        comparison = Table(
            [["Klassisch", "Quantencomputer"],
             [time_classical, time_quantum]],
            col_labels=[Text("Algorithmus"), Text("Zeitbedarf")],
            include_outer_lines=True
        ).scale(0.6)
        
        self.play(
            FadeOut(primes),
            complexity.animate.scale(0.7).to_edge(UP),
            FadeIn(comparison)
        )
        self.wait(3)

        # Quantenvorteil-Erklärung
        shor_eq = MathTex(
            "\\text{Zeit} \\propto (\\log N)^3", 
            color=GREEN
        ).next_to(comparison, DOWN)
        
        self.play(Write(shor_eq))
        box_note = Text("* Mit Shor-Algorithmus und 20 Mio. fehlerkorrigierten Qubits", font_size=18).to_edge(DOWN)
        self.play(Write(box_note))
        self.wait(3)


from manim import *

class RSADemo(Scene):
    def construct(self):
        # Schritt 1: Google-Link mit farbigem "s"
        google_text = Text("https://www.google.com", font_size=36)
        self.play(Write(google_text))
        self.wait(1)
        
        s_index = google_text.text.index("s")
        s_char = google_text.chars[s_index]
        self.play(s_char.animate.set_color(YELLOW))
        self.wait(1)
        self.play(FadeOut(google_text))
        self.wait(0.5)

        # RSA Titel
        title = Text("RSA", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Linke Seite
        left_pic = ImageMobject("person.png").set_height(2)
        left_numbers = VGroup(  # Nur die Text-Elemente in VGroup
            Text("101", font_size=60),
            Text("×", font_size=60),
            Text("103", font_size=60)
        ).arrange(RIGHT, buff=0.5)
        
        # Gruppe aus Bild und Zahlen mit Group statt VGroup
        left_group = Group(left_pic, left_numbers).arrange(RIGHT, buff=1).to_edge(LEFT, buff=1)
        self.play(FadeIn(left_group))
        self.wait(1)

        # Rechte Seite
        right_pic = ImageMobject("person.png").set_height(2)
        right_numbers = VGroup(
            Text("107", font_size=60),
            Text("×", font_size=60),
            Text("109", font_size=60)
        ).arrange(RIGHT, buff=0.5)
        
        right_group = Group(right_pic, right_numbers).arrange(RIGHT, buff=1).to_edge(RIGHT, buff=1)
        self.play(FadeIn(right_group))
        self.wait(1)

        # Ergebnisse
        left_result = Text("10403", font_size=60).move_to(left_numbers.get_center())
        right_result = Text("11663", font_size=60).move_to(right_numbers.get_center())
        self.play(
            Transform(left_numbers, left_result),
            Transform(right_numbers, right_result)
        )
        self.wait(2)


from manim import *




from manim import *
from manim import *

class RSAPrimeFactorization(Scene):
    def construct(self):
        # Die RSA-2048 Zahl als langer String
        rsa_number = (
            "251959084756578934940271832400483985714292821262040320277771378360436620207075955562640185258807844069182906412495150821892985591491761845028084891200728449926873928072877767359714183472702618963750149718246911650776133798590957000973304597488084284017974291006424586918171951187461215151726546322822168699875491824224336372590851418654620435767984233871847744479207399342365848238242812981631501067481045166037730605619676256133844143603833904414952634432190114657544454178424020924616515723350778707749817125772467962926386356373289912154831438167899885040445364023527381951378636564391212010397122822120720357"
        )

        # Bestimme, wieviele Ziffern pro Zeile angezeigt werden sollen
        digits_per_line = 70
        # Teile die Zahl in mehrere Zeilen auf
        lines_list = [
            rsa_number[i : i + digits_per_line]
            for i in range(0, len(rsa_number), digits_per_line)
        ]

        # Erstelle für jede Zeile ein Textobjekt (monospaced für gleichmäßige Darstellung)
        rsa_text_lines = VGroup(*[
            Text(line, font_size=24)
            for line in lines_list
        ])
        # Ordne die Zeilen vertikal untereinander an
        rsa_text_lines.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        rsa_text_lines.move_to(ORIGIN)

        # Blende die vollständige Zahl über die ganze Folie ein
        self.play(Write(rsa_text_lines))
        self.wait(2)

        # Verkleinere die Zahl und verschiebe sie nach oben, damit Platz für die Anmerkungen entsteht
        self.play(rsa_text_lines.animate.scale(0.5).to_edge(UP))
        self.wait(1)

        # Erstelle die Anmerkungstexte für die Laufzeiten
        super_text = Text("Supercomputer: 300 Billionen Jahre", font_size=32)
        quantum_text = Text("Quantencomputer: 8 Stunden", font_size=32)
        annotations = VGroup(super_text, quantum_text)
        annotations.arrange(DOWN, center=True, buff=0.3)
        annotations.next_to(rsa_text_lines, DOWN, buff=0.5)

        # Blende die Anmerkungen ein
        self.play(Write(annotations))
        self.wait(3)



class Fazit(Scene):
    def construct(self):
        # Titel
        title = Text("Fazit", font_size=48)
        title.to_edge(UP)
        underline = Line(title.get_left(), title.get_right(), color=WHITE)
        underline.next_to(title, DOWN, buff=0.1)
        
        # Gliederungspunkte
        points = VGroup(
            Text("Vielversprechende Technologie"),
            Text("2. Aufbau"),
            Text("3. Aktueller Stand"),
            Text("4. Einsatzmöglichkeiten"),
            Text("5. Fazit")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        points.next_to(underline, DOWN, buff=0.5)
        
        # Animation
        self.play(Write(title))
        self.play(Create(underline))
        self.wait(0.5)
        for point in points:
            self.play(FadeIn(point, shift=UP*0.5))
            self.wait(0.3)

        self.next_slide()

from manim import *

class RSA(Scene):
    def construct(self):
        # Load person image (assuming person.png is in the same directory)
        person_image = ImageMobject("person.png").scale(0.5)

        person1 = person_image.copy().to_edge(LEFT, buff=2)
        person2 = person_image.copy().to_edge(RIGHT, buff=2)

        self.add(person1, person2)

        # --- Title RSA ---
        title = Text("RSA", font_size=48).to_edge(UP)
        self.play(Write(title))

        prime_numbers_left = VGroup(
            Text("1814159566", font_size=12),
            Text("8199703079", font_size=12),
            Text("8268171682", font_size=12),
            Text("2107016038", font_size=12),
            Text("9201705043", font_size=12),
            Text("9145746256", font_size=12),
            Text("3485198126", font_size=12),
            Text("9167351672", font_size=12),
            Text("6021561952", font_size=12),
            Text("3429714031", font_size=12),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(person1, RIGHT)

        prime_numbers2_left = VGroup(
            Text("2074722246", font_size=12),
            Text("7734852078", font_size=12),
            Text("2169522210", font_size=12),
            Text("7608587480", font_size=12),
            Text("9964747211", font_size=12),
            Text("1729275299", font_size=12),
            Text("2589912196", font_size=12),
            Text("6847505496", font_size=12),
            Text("5831008441", font_size=12),
            Text("6732550077", font_size=12),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(prime_numbers_left, LEFT, buff=0.5)

        prime_numbers_group_left = VGroup(prime_numbers2_left, prime_numbers_left)
        prime_numbers_group_left.move_to(person1.get_center() + RIGHT * 2 + UP * 0.5)

        multiply_symbol_private_left = MathTex(r"\times").scale(1.0).move_to(prime_numbers_group_left.get_center())


        prime_numbers_right = VGroup(
            Text("2193992993", font_size=12),
            Text("2186043108", font_size=12),
            Text("8446186461", font_size=12),
            Text("8001945131", font_size=12),
            Text("7909252825", font_size=12),
            Text("3176867916", font_size=12),
            Text("9054389241", font_size=12),
            Text("5278952221", font_size=12),
            Text("6947672369", font_size=12),
            Text("1605898517", font_size=12),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(person2, LEFT)

        prime_numbers2_right = VGroup(
            Text("5202642720", font_size=12),
            Text("9861890870", font_size=12),
            Text("3483783233", font_size=12),
            Text("7828472969", font_size=12),
            Text("8009109265", font_size=12),
            Text("0136196787", font_size=12),
            Text("2059486045", font_size=12),
            Text("7131454501", font_size=12),
            Text("1671248868", font_size=12),
            Text("5004691423", font_size=12),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(prime_numbers_right, RIGHT, buff=0.5)

        prime_numbers_group_right = VGroup(prime_numbers2_right, prime_numbers_right)
        prime_numbers_group_right.move_to(person2.get_center() + LEFT * 2 + UP * 0.5)

        multiply_symbol_private_right = MathTex(r"\times").scale(1.0).move_to(prime_numbers_group_right.get_center())

        product_number_left = VGroup(
            Text("37638772124783414645", font_size=12, color=GREEN),
            Text("94602454228914655621", font_size=12, color=GREEN),
            Text("76077694603899107034", font_size=12, color=GREEN),
            Text("95419162622350200649", font_size=12, color=GREEN),
            Text("03144856319081877639", font_size=12, color=GREEN),
            Text("00098991180121826015", font_size=12, color=GREEN),
            Text("25803794988738266933", font_size=12, color=GREEN),
            Text("07503278567032707173", font_size=12, color=GREEN),
            Text("14437116783608458370", font_size=12, color=GREEN),
            Text("8840781213497030387", font_size=12, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(person1, LEFT)


        product_number_right = VGroup(
            Text("11414561676063473033", font_size=12, color=GREEN),
            Text("52674881788600518840", font_size=12, color=GREEN),
            Text("22489535754160389636", font_size=12, color=GREEN),
            Text("9233196695168894940", font_size=12, color=GREEN),
            Text("5257644735013863752", font_size=12, color=GREEN),
            Text("63147220836758611463", font_size=12, color=GREEN),
            Text("61449934998092861696", font_size=12, color=GREEN),
            Text("51846913045826286068", font_size=12, color=GREEN),
            Text("62829147745745985031", font_size=12, color=GREEN),
            Text("44112224964238319691", font_size=12, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(person2, RIGHT)

        self.play(FadeIn(prime_numbers_group_left), FadeIn(prime_numbers_group_right))
        self.wait(2)
        self.play(FadeIn(multiply_symbol_private_left), FadeIn(multiply_symbol_private_right))
        self.wait(2)
        self.play(FadeIn(product_number_left.move_to(person1.get_center() + LEFT * 2 + UP * 0.5)), FadeIn(product_number_right.move_to(person2.get_center() + RIGHT * 2 + UP * 0.5)))
        self.wait(2)

        # Original message setup
        nachricht = VGroup(
            Text("Hallo, Welt!", font_size=12),
            Text("Dies ist eine geheime Nachricht", font_size=12),
            Text("Ich hoffe es geht dir gut", font_size=12),
            Text("Beste Grüße", font_size=12),
            Text("Max Mustermann", font_size=12),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(person1, DOWN, buff=0.5)

        self.play(FadeIn(nachricht))
        self.wait(2)
        
        # Store original positions
        original_product_right_pos = product_number_right.get_center()
        original_prime_right_pos = prime_numbers_group_right.get_center()

        # Encryption animation
        self.play(
            product_number_right.animate.next_to(nachricht, UP, buff=0.1),
            run_time=1.5
        )
        
        encrypted_message = VGroup(
            Text(";Y5(5zq.:ZpN*h7-]6wG<t", font_size=12),
            Text("H$+U6B` oi6` i;!E,Q90#7?", font_size=12),
            Text("gu#0jZ|BQ`Mw_,M$hmy}", font_size=12),
            Text("T@T#b<YN(M;RVvH?", font_size=12),
            Text("G`:ZzC_`DYYIczViw#}", font_size=12),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(nachricht.get_center())

        self.play(
            TransformMatchingShapes(nachricht, encrypted_message),
            product_number_right.animate.move_to(original_product_right_pos),
            run_time=2
        )
        
        # Move encrypted message to receiver
        self.play(
            encrypted_message.animate.next_to(person2, DOWN, buff=0.5),
            run_time=1.5
        )
        self.wait(1)

        # Decryption animation
        self.play(
            prime_numbers_group_right.animate.next_to(encrypted_message, UP, buff=0.1),
            run_time=1.5
        )
        
        decrypted_message = nachricht.copy().next_to(person2, DOWN, buff=0.5)
        self.play(
            TransformMatchingShapes(encrypted_message, decrypted_message),
            prime_numbers_group_right.animate.move_to(original_prime_right_pos),
            run_time=2
        )
        self.wait(2)

from manim import *
from manim import *
class Quellen(Scene):
    def construct(self):
        # Titel erstellen
        title = Text("Quellen", font_size=48)
        title.to_edge(UP)
        underline = Line(title.get_left(), title.get_right(), color=WHITE)
        underline.next_to(title, DOWN, buff=0.1)
        
        self.play(Write(title), Create(underline))
        self.wait(1)

        # Vollständig überprüfte Quellenangaben
        quellen = VGroup(
            Text("DigiCert. (2024). Post-Quantum Cryptography: Preparing for a Secure Future. Abgerufen von https://www.digicert.com/de/insights/post-quantum-cryptography", font_size=18),
            Text("Gidney, C., & Ekerå, M. (2019). How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits. arXiv:1905.09749", font_size=18),
            Text("Pennylane. (2023). Quantum Simulations with Trapped Ions. Abgerufen von https://pennylane.ai/qml/demos/tutorial_trapped_ions", font_size=18),
            Text("Photonworld. (2024). Technische Grundlagen der Ionenfallen-Quantencomputer. Abgerufen von https://photonworld.de/pdf/tech-36-d-06-web", font_size=18),
            Text("Marchenkova, A. [Anastasia Marchenkova]. (2023). Quantum Computing Explained [Video]. YouTube. https://www.youtube.com/watch?v=-UrdExQW0cs", font_size=18),
            Text("Quantum Computing Report. (2024). Ion Trap Quantum Computers [Video]. YouTube. https://www.youtube.com/watch?v=lvTqbM5Dq4Q", font_size=18),
            Text("Monroe, C., et al. (2024). Logical quantum processor based on reconfigurable atom arrays. Nature, 627(7992), 207-212.", font_size=18),
            Text("Quarks/WDR. (2023). So funktioniert ein Quantencomputer. Abgerufen von https://www.quarks.de/technik/faq-quantencomputer", font_size=18),
            Text("Google Quantum AI Team. (2024). Advancing Quantum Computing with the Willow Chip. Google Research Blog. Abgerufen von https://blog.google/technology/research", font_size=18),
            Text("Universität Innsbruck. (2023). Quantum Computing with Trapped Ions [Video]. YouTube. https://www.youtube.com/watch?v=g_IaVepNDT4", font_size=18),
            Text("IBM Research. (2024). Quantum Error Correction Basics [Video]. YouTube. https://www.youtube.com/watch?v=rYW2NlU359U", font_size=18),
            Text("Karlsruher Physikkurs. (2024). Grundlagen der Quantencomputer-Architektur. Abgerufen von https://www.karlsruher-physikkurs.de/quantencomputer", font_size=18),
            Text("TechHQ. (2025). Google's Quantum Breakthrough Analysis. Abgerufen von https://techhq.com/2025/01/google-quantum-breakthrough", font_size=18)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).scale(0.6)

        # Zentrierung des gesamten Blocks
        quellen.next_to(underline, DOWN, buff=0.3)
        quellen.to_edge(LEFT, buff=0.5)  # Linksbündig mit etwas Abstand zum Rand
        
        self.play(FadeIn(quellen, shift=DOWN))
        self.wait(3)