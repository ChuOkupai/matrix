# Projection Matrix Display

This software is intended to provide a way to check that a 3D projection matrix is valid.

To perform the test, place the matrix into a file called `proj`. Example:

```
1.0, 0.0, 0.0, 0.0
0.0, 1.0, 0.0, 0.0
0.0, 0.0, 1.0, 0.0
0.0, 0.0, 0.0, 1.0
```

(The above matrix will not work properly for a 3D projection but its format is correct)

If the matrix is correct, the display will show a 3D projection of the 42AI organization's logo.

## Controls

- **Esc**: Quit the program
- **Arrow Up**/**W**: Move forward
- **Arrow Down**/**S**: Move backward
- **Arrow Left**/**A**: Move left
- **Arrow Right**/**D**: Move right
- **Mouse**: Look around
