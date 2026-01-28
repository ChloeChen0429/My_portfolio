# Project Title - NinJa Frog 

![Xnip2025-02-12_21-27-06](https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/832ae291-a7d3-4501-8a0a-2d16dbd64db2)

|Team member    |Discussion & Research|Concept|Unity Scene Building|Unity Scene & Component Code|Arduino Code & Making|Unity Arduino Communication & Interaction Code|Debugging & Testing|GitHub Writing|
| :---          | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | 
| Manyi Lin     | ✅   | ✅   |  ✅    | ✅   |       |      |  ✅   |     |  
| Yuxin Chen    | ✅   | ✅   | ✅   |   ✅   |       |      |  ✅   |    |   
| Zenghou Luan  | ✅   | ✅   |     |    | ✅    | ✅   |    ✅  | ✅   | 

---

## Overview & Project Description
### Interaction & Rules:

Ninja Frog is a 2D platformer where players control a frog using an gyroscope sensor to move and jump through hand gestures:

	•	Tilting the hand left → The frog moves left
 
	•	Tilting the hand right → The frog moves right
 
	•	Quickly lifting the hand up → The frog jumps

The rule is to avoid spikes and rotating gears, prevent death, collect cherries along the way, and ultimately reach the finish line. 

The game currently features two levels with increasing difficulty, testing the player’s reaction speed and precision.

### Concepts and Goals:

The hand gesture control mechanism in Ninja Frog is inspired by an ancient Chinese saying:

##### “翻手为云，覆手为雨” —— “With a flip of the hand, clouds form; with another, rain falls.”

<img width="1008" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/38028625-e0fa-4596-9c4f-f64fb58c4072">

Originally, this phrase described the unpredictable control of those in power. 

In the game, this interaction serves not only as a gameplay mechanic but also as a metaphor, encouraging players to reflect on the war.

Ninjas, much like soldiers in real-world battlefields, may never realize the invisible hand manipulating their fate. 

The spikes and rotating gears are dangers and conflicts within political struggles. 

They relentlessly tear apart the ninja frog’s path forward, just as war and power struggles devastate countless lives.
 
---
## Supplies & Materials

### Components Used:  
- **Arduino Board**:RF-NANO (Very small in size and suitable for manipulation in the hand.)
- **Sensor**:  MPU-6050 (gyroscope sensor)
- **Additional Materials**: Jump wires, breadboards

### Images:  
<img width="631" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/b74a5948-4015-4d51-9217-654d5c19b724">

---

## Process

### Concept

Hand movements: From manipulation to awakening

<img width="1345" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/668a7eea-1a41-4ec5-88e0-61bb0a4d7d7c">


"Ninja Frog" is not only an allegory about political games, but also a practice of personal awakening. Hand movements are not only a symbol of power, but also a manifestation of the player's inner strength. Through the interaction between the hand and Ninja Frog, players gradually experience a transformation from manipulation to awakening.

The dilemma of manipulation: At the initial stage of the game, players may feel that there is a certain disconnection between hand movements and the movement of Ninja Frog. This is just like our state in political games - being carried away by external forces and losing control of our own destiny.
The opportunity for awakening: Every failure is an opportunity for awakening. When Ninja Frog falls into spikes or gears, players need to reflect on the power behind hand movements - is it unconscious manipulation or the pursuit of balance? This reflection guides players to shift from simple operation to the awareness of inner strength.

The practice of peace: As the game progresses, players gradually master the synchronization between the hand and Ninja Frog, and the movements become smooth and precise. This symbolizes the transformation from manipulation to awakening - when players realize the power of hand movements and learn to use them in a peaceful and balanced way, Ninja Frog's journey becomes a practice of peace.

The end: From political games to peaceful awakening.

The ultimate goal of the game is to guide Ninja Frog to reach the destination. This journey is not only a test of operating skills, but also a pursuit of peace and awakening. Cherry blossoms as collectibles symbolize hope and life, and the end symbolizes the realm of peace and unity.
Through the interaction between the hand and Ninja Frog, players experience a profound sense of satisfaction, as if completing a practice from political games to peaceful awakening. "Ninja Frog" interprets an important truth with the game mechanism - true power does not come from manipulation and struggle, but from the awakening of peace and balance.

---

### Unity Scene Building

<img width="1465" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/67692c67-a68b-4d2a-8731-98f8534ccc53">

In this project, we created a 2D platform game scene with a pixel art style overall. The scene is composed of multiple key parts:

 • Background
 
The background is built using Tilemap. Repeated grass and ground textures are used to form a game environment with a sense of hierarchy. The background layer is sorted behind the player character to avoid visual confusion.

 • Platform
 
The terrain is drawn using the Tilemap tool. Collision detection (Collider) is set up to ensure that the player can stand and jump normally. The distribution design of the platform increases the challenge of the game.

 • Items
 
Multiple collectible items (such as cherries) are arranged in the scene to enhance the interestingness of the game. Items will disappear after collision and update the player's score at the same time. The current score will be displayed in real time in the UI.

 • Traps
 
To increase the difficulty of the game, we added spike traps in the scene. When the player touches a trap, a death animation will be triggered, and the level will restart after the animation ends.

 • Moving Platform
 
A moving platform is also set up in the scene. The player can move along with the platform, bringing more interactive experience and challenges.

---

### Unity Scene & Component Code

To achieve the core functions of the game, we wrote multiple scripts to control functions such as player movement, item collection, death and rebirth, and platform following respectively.

<img width="651" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/78bbd38a-0e48-4d31-8001-9fed064f8510">

#### 1. Player character control

The PlayerMoment script implements the basic control logic for the player, including left-right movement, jumping, and animation state switching.

 - Left-right movement: Controls the horizontal speed of the character through Rigidbody2D.
   
 - Jumping: Detects whether the character is on the ground and allows for a single jump.
   
 - Animation state switching: Uses Animator to switch character animations such as idle, running, jumping, and falling.
   
Core code example:

```
private void Update()
{
    dirX = Input.GetAxisRaw("Horizontal");
    rb.velocity = new Vector2(dirX * moveSpeed, rb.velocity.y);

    if (Input.GetButtonDown("Jump") && IsGrounded())
    {
        rb.velocity = new Vector2(rb.velocity.x, jumpForce);
    }

    UpdateAnimationState();
}
```

#### 2. Prop collection function

The item_collector script is used to detect collisions between players and props and update the UI score display. Every time a player collects a cherry, the score increases and the prop is destroyed.

Core code example:

```
private void OnTriggerEnter2D(Collider2D collision)
{
    if (collision.gameObject.CompareTag("Cherry"))
    {
        Destroy(collision.gameObject);
        score++;
        cherriesText.text = "Cherries: " + score;
    }
}
```

#### 3. Player death and rebirth

The PlayerLife script implements a respawn mechanism after the player character dies. When the player touches a trap, a death animation is triggered and the level restarts after 2 seconds.

Core code example:

```
private void Die()
{
    rb.bodyType = RigidbodyType2D.Static;
    anim.SetTrigger("death");
    Invoke("RestartLevel", 2f);
}

private void RestartLevel()
{
    SceneManager.LoadScene(SceneManager.GetActiveScene().name);
}
```

4. Platform following function

The StickyPlatform script is used to achieve the following effect when the player stands on a moving platform. When the player enters the platform, the parent object becomes the platform; when the player leaves the platform, the parent object is set to null. 

Core code example:

```
private void OnTriggerEnter2D(Collider2D collision)
{
    if (collision.gameObject.name == "Player")
    {
        collision.gameObject.transform.SetParent(transform);
    }
}

private void OnTriggerExit2D(Collider2D collision)
{
    if (collision.gameObject.name == "Player")
    {
        collision.gameObject.transform.SetParent(null);
    }
}
```

---

### Arduino Code & Making

|MPU6050 pins  |Arduino pins|
| :---          | :--- | 
|VCC     |5V | 
| GND   | GND   |
| SCL  | A5 | 
| SDA  | A4   | 

![image](https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/eb352c5f-7cb4-4077-a566-3fc8f1338d5f)

Code structure:

Read the acceleration data of the MPU6050 sensor.

Smooth the data through low-pass filtering to reduce noise.

Calculate the control signal of the X-axis and limit its range.

Determine whether a jump has occurred through the acceleration of the Z-axis.

Output "CTRL:" (control signal) and "JUMP:" (jump signal) through the serial port.

"The value after 'CTRL:' represents the tilt control signal of the X-axis (-1 to 1). 

The 1 or 0 after 'JUMP:' indicates whether a jump is detected."

---

### Unity Arduino Communication & Action Code

#### 1. Serial communication

serialPort.Open(): Open the serial port to establish communication with Arduino.

serialPort.ReadLine(): Read the string data sent by Arduino.

ParseSensorData(): Parse the data and use the CTRL value for controlling left and right movement and the JUMP value for jump judgment.

#### 2. action control

dirX = controlValue Updates horizontal movement speed based on sensor values.

rb.velocity Controls rigid body movement.

IsGrounded() Detects whether the character is on the ground through BoxCast.

UpdateAnimationState() Updates animations according to states.

#### 3. Game interaction

The movement direction of the character is determined by the data provided by the Arduino sensor.

The jumping state is only allowed to be triggered when IsGrounded() returns true.

---

### Debugging & Testing

|Problem|	Solution|
| :---          | :--- |
|Arduino cannot send data.|	Check Serial.begin(115200); and ensure there is a line break at the end of Serial.println().|
|Data cannot be received on the Unity side.|Ensure that the port number is correct (Mac /dev/cu.usbserial-XXX) and try Debug.Log(data);|
|Error in parsing data format.|	Add try-catch to capture exceptions and use Debug.Log(data); to check the format.|
|The character is immobile or the jump function fails.|	Ensure that controlValue and isJumping are updated correctly and that jumpForce is large enough.|
|High data transmission delay|	Optimize Update(), use asynchronous reading and reduce the frequency of Serial.println().|

### Component production

<img width="813" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/389ee0e2-b568-47c0-bc28-79e6e17e2087">

---

## Video Demonstration


https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/ed3d497f-d800-4c3a-b271-ffda3cc545d1


---

## Final Images

<img width="1266" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/b8e8c199-ab8c-4cfb-b1b2-012564a199ae">

---

## Arduino Code
### Arduino MPU6050 Code
[Arduino Code file](https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/blob/7c3330bd2f0bd3d343b5e5910557fc3e2c4cd3a5/CODE/unity%202D%20arduino)

```
#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

// Filtering parameters
float accelSensitivity = 16384.0; // Sensitivity for ±2g
float alpha = 0.2;                // Low-pass filter coefficient
float filteredX = 0;              // Filtered X-axis value
float filteredZ = 0;              // Filtered Z-axis value

// Jump detection parameters
float jumpThreshold = 1.5;        // Jump detection threshold (in g)
bool isJumping = false;           // Jump state flag

void setup() {
  Serial.begin(115200);
  Wire.begin();

  // Initialize MPU6050
  mpu.initialize();

  // Verify connection
  if (!mpu.testConnection()) {
    Serial.println("MPU6050 connection failed! Please check wiring.");
    while (1);
  }

  // Calibrate accelerometer (Run this while the sensor is placed flat on a table)
  mpu.setXAccelOffset(-1100);
  mpu.setYAccelOffset(-1029);
  mpu.setZAccelOffset(1330);
}

void loop() {
  // Read raw acceleration data
  int16_t ax, ay, az;
  mpu.getAcceleration(&ax, &ay, &az);

  // Convert to g-values and apply low-pass filtering
  float rawX = ax / accelSensitivity;
  float rawZ = az / accelSensitivity;
  filteredX = alpha * rawX + (1 - alpha) * filteredX;
  filteredZ = alpha * rawZ + (1 - alpha) * filteredZ;

  // Convert to control signal (range: -1 to 1)
  float controlValue = constrain(filteredX * 2.5, -1, 1);

  // Detect jump
  if (filteredZ > jumpThreshold && !isJumping) {
    isJumping = true;
  } else if (filteredZ <= jumpThreshold && isJumping) {
    isJumping = false;
  }

  // Send data to serial monitor (format: CTRL:value, JUMP:state)
  Serial.print("CTRL:");
  Serial.print(controlValue, 2); // Control signal
  Serial.print(",JUMP:");
  Serial.println(isJumping ? "1" : "0"); // Jump signal

  delay(20); // Maintain ~50Hz update rate
}
```

---

### Unity Arduino communication & action
[Unity Arduino communication & action code](https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/blob/83d933a9b19f49646c45ec1d87b7cb194d49df2d/CODE/Unity%20Arduino%20communication%20%26%20action%20code)
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO.Ports;

public class PlayerMovement : MonoBehaviour
{
    private Rigidbody2D rb;
    private BoxCollider2D coll;
    private SpriteRenderer sprite;
    private Animator anim;

    [SerializeField] private LayerMask jumpableGround;

    private float dirX = 0f;
    [SerializeField] private float moveSpeed = 7f;
    [SerializeField] private float jumpForce = 7f;

    private enum MovementState { idle, running, jumping, falling }
    [SerializeField] private AudioSource jumpSoundEffect;

    // Serial communication
    private SerialPort serialPort;
    private string[] sensorData;
    private float controlValue = 0f;
    private bool isJumping = false;

    // Start is called before the first frame update
    private void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        coll = GetComponent<BoxCollider2D>();
        sprite = GetComponent<SpriteRenderer>();
        anim = GetComponent<Animator>();

        // Initialize serial port
        serialPort = new SerialPort("/dev/cu.usbserial-110", 115200); 
        serialPort.Open();
    }

    private void Update()
    {
        // Read data from serial port
        if (serialPort.IsOpen && serialPort.BytesToRead > 0)
        {
            string data = serialPort.ReadLine();
            ParseSensorData(data);
        }

        // Move player based on control input
        dirX = controlValue;
        rb.velocity = new Vector2(-dirX * moveSpeed, rb.velocity.y);

        // Handle jumping
        if (isJumping && IsGrounded())
        {
            jumpSoundEffect.Play();
            rb.velocity = new Vector2(rb.velocity.x, jumpForce);
        }

        UpdateAnimationState();
    }

    private void ParseSensorData(string data)
    {
        // Data format: CTRL:value,JUMP:state
        sensorData = data.Split(',');

        if (sensorData.Length >= 2)
        {
            string[] ctrlData = sensorData[0].Split(':');
            if (ctrlData.Length >= 2)
            {
                float.TryParse(ctrlData[1], out controlValue);
            }

            string[] jumpData = sensorData[1].Split(':');
            if (jumpData.Length >= 2)
            {
                int jumpState;
                if (int.TryParse(jumpData[1], out jumpState))
                {
                    isJumping = jumpState == 1;
                }
            }
        }
    }

    private void UpdateAnimationState()
    {
        MovementState state;

        if (dirX > 0f)
        {
            state = MovementState.running;
            sprite.flipX = false;
        }
        else if (dirX < 0f)
        {
            state = MovementState.running;
            sprite.flipX = true;
        }
        else
        {
            state = MovementState.idle;
        }

        if (rb.velocity.y > .1f)
        {
            state = MovementState.jumping;
        }
        else if (rb.velocity.y < -.1f)
        {
            state = MovementState.falling;
        }

        anim.SetInteger("state", (int)state);
    }

    private bool IsGrounded()
    {
        return Physics2D.BoxCast(coll.bounds.center, coll.bounds.size, 0f, Vector2.down, .1f, jumpableGround);
    }

    private void OnDestroy()
    {
        if (serialPort != null && serialPort.IsOpen)
        {
            serialPort.Close();
        }
    }
}
```

## Link to Unity Files

[LINK UNITY FILES](https://drive.google.com/file/d/1-XVVaLMuIbDttGsVcyZim7nB-50qqmHc/view?usp=sharing)

<img width="1382" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/b1225f12-9831-4acc-a4b9-5d798bb40470">

---

## Design Justification 
### 1. Reflection on the production process:
   
Before the final game design was produced, we conducted a 3D interaction experiment and created a simple 3D scene, including a straight path as the rolling area for the small ball. We also added basic light sources and ambient light to ensure that the scene is clearly visible.

<img width="1456" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/80fb0a3e-4970-4f17-96c9-ab668d8b2a33">

![Xnip2025-02-12_20-45-26](https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/50b4cdd0-8593-4441-b19e-e435915ea3b9)


#### 1.1 Scene and Obstacle Design

Use Unity's 3D Cube to build obstacles and walls to enhance the game's challenge. By adjusting the scaling of objects, design obstacles of different shapes and heights to make the levels more variable.

#### 1.2 Visual effect optimization

Adjust the material and texture of obstacles to distinguish them from the ground and enhance the visual layering. Give the ball a red material to make it more recognizable and attractive.

#### 1.3 Mechanism code implementation (Unity Scene & Component Code)
   
Ball control script: Use the rigid body component to control the physical movement of the ball and write a script to read Arduino input to achieve direction adjustment.

Arduino integration: Read Arduino sensor data through serial communication and map it to the ball's movement instructions to achieve physical interaction control, enabling players to control the ball through external devices.

After such optimization, the overall interaction is clearer and more fluid.      



https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/5ee79b1a-ba75-4ee2-a184-fe181a97245e



We have obtained good interaction effects. However, we have encountered difficulties in concept and artistic expression. Because this game is somewhat common and more like a time-killing game, we haven't been able to obtain more ideological expressions from this game.

So, we decided to start from the concept itself and optimize the game. Later, we focused on the current world issue of war. We want to express the phenomenon that in political games, the thoughts and actions of those in power often affect the life and death and fate of countless people. Therefore, we think that the 2D game method can better express this concept. Because players are in a three-dimensional world and the characters in the game are in a two-dimensional world, just like political figures in real life are in the upper layer and control soldiers who don't know the real situation.

In game design, we combine players' gesture control with the actions of game characters to create an experience that seems to be in control but is actually out of control. Initially, players will feel absolute control over the characters. But as the game progresses, they will realize that the fate of the characters is not entirely determined by themselves but is influenced by external forces. The actions of characters on the battlefield may be restricted due to changes in commands and even lead to inevitable sacrifice.

In the end, the outcome of the game is not simply a matter of victory or defeat. Instead, it makes players reflect on the role they have played throughout the process. Will they become a cold controller or seek another possibility after awakening? The core concept of the game - from control to awakening - runs through the entire experience. It is hoped that players can resonate during the process and have a deeper understanding of the power structure in the real world.

### 2. Reflection on the final result:

<img width="666" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/5aa9d8f9-b90e-497a-9859-fd03f6c49dc5">

#### 2.1 Reflection and improvement on teamwork

Our team members have relatively clear divisions of labor. Each person is responsible for specific tasks such as Unity development, Arduino programming, concept design, and so on. However, in the actual development process, this division of labor sometimes appears too fixed, resulting in a lack of flexible collaboration among members. For example, when encountering cross-module problems, additional time is needed for coordination and communication. Our team members can communicate problems in a timely manner and solve them together, but on some complex issues, communication efficiency is still relatively low. For example, when debugging the interaction between Unity and Arduino, due to a lack of in-depth understanding of each other's modules, both parties need to repeatedly confirm details.

#### 2.2 Reflection and improvement on interaction optimization

• Precision of gesture control: Although the gesture control mechanism brings a novel experience to players, in actual operation, the precision of gesture recognition still needs to be improved. For example, when players are moving or jumping quickly, misoperations or response delays may occur.

• Interaction complexity: As the game difficulty increases, the complexity of gesture operations also increases accordingly. Some players may find the operation too complex and difficult to master, thus affecting the game experience.

• Optimize gesture recognition algorithm: Further optimize the gesture recognition algorithm in Arduino code to improve the accuracy and real-time performance of data processing. For example, more complex filtering algorithms or machine learning models can be introduced to reduce misoperations and delays.

• Enhance interaction feedback: Add more interaction feedback mechanisms. For example, after players complete gesture operations, through visual effects or vibration feedback, players can clearly feel that the operation has been recognized.

#### 3.3 Conceptual expression reflection and improvement

##### 3.3.1 Conceptual expression reflection

• Conceptual abstraction: The game's theme of "From manipulation to awakening" is relatively abstract, and some players may find it difficult to understand its deep meaning in a short time. These metaphors may not be intuitive enough for players without relevant background knowledge.

• Insufficient emotional resonance: Although the game mechanism and theme design have a certain depth of thought, in actual experience, some players may pay more attention to the operability of the game and overlook the emotional and ideological expressions behind the game.

##### 3.3.2 Conceptual expression improvement space

• Add theme guidance: Before the game starts, clearly introduce the game's theme and background through a short animation or text description. For example, a concept of "with great power comes great responsibility" can be shown through an opening animation to help players better understand the deep meaning of the game.

• Strengthen emotional resonance: During the game, enhance emotional resonance through character dialogue, background music, and plot development. For example, some inner monologues or narrations of characters can be added to the game to guide players to think about the real meaning behind the game.

• Enrich metaphorical expressions: Further enrich the metaphorical elements in the game to make them more intuitive and easy to understand. For example, more scene details (such as war ruins, political symbols, etc.) can be added to strengthen the theme expression of the game.

#### Our team has spent a lot of time on this game and also likes our output very much. We hope to continue to improve and perfect our game according to these areas that can be improved as summarized, in our spare time.


