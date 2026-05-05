#include <stdio.h>
#include <string.h>

const char* thermostat(int temp, int target) {
    int hysteresis = 2;

    if (temp > target + hysteresis)
        return "Cooling";
    else if (temp < target - hysteresis)
        return "Heating";
    else
        return "Idle";
}

void assertEqual(const char* expected, const char* actual, const char* testName) {
    if (strcmp(expected, actual) == 0)
        printf("PASS: %s\n", testName);
    else
        printf("FAIL: %s (Expected %s, got %s)\n", testName, expected, actual);
}

int main() {
    int target = 72;

    assertEqual("Cooling", thermostat(76, target), "Cooling test");
    assertEqual("Heating", thermostat(68, target), "Heating test");
    assertEqual("Idle", thermostat(72, target), "Exact target");
    assertEqual("Idle", thermostat(73, target), "Upper hysteresis");
    assertEqual("Idle", thermostat(71, target), "Lower hysteresis");

    return 0;
}