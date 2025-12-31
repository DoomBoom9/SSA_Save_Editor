# SSA_Save_Editor
 A savefile editor for Skylanders Spyro's Adventure

 this is a work in progress, currently only the checksum fixer/validator works.

 make sure to have python3 installed

 make sure that the savefile you input into the program is the decrypted save slot from dolphin or is a decrypted save slot from segher's tachtig.

 to run the checksum validator/fixer:
    open terminal
    ```
    python3 C:\path\to\checksum_calc.py C:\path\to\Save_Slot_1
    ```

 alternatively for linux, mac:
    open terminal
    ```
    cd C:\path\to\project
    ```
    ```
    chmod +x checksum_calc.py
    ```
    ```
    ./checksum_calc.py Save_Slot_1
    ```