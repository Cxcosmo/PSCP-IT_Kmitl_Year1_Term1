"""Niwarn World"""
import math
def x(n) :
    """X"""
    return 2 + ((math.log((n**2),2)) / ((2 * n) * math.log(n, 2)))
def y(n, s) :
    """Y"""
    return (math.sin(math.radians(30)) + ((2 * s) ** 0.5)) / (x(n) + 3)
def z(k) :
    """Z"""
    return (y(k, k) ** 2) + ((8456 * (x(k) ** 4)) / (24 * k))
def main(n,s,k) :
    """Niwarn World"""
    print(f"X: {x(n):.1f}, Y: {y(n, s):.1f}, Z: {z(k):.1f}")
main(float(input()), float(input()), float(input()))
