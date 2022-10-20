import 'package:flutter/material.dart';

void main() {
  runApp(Bayrak());
}

class Bayrak extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Center(
        child: TurkBayragi(
          G: 200,
        ),
      ),
    );
  }
}

class TurkBayragi extends StatelessWidget {
  final double G;
  TurkBayragi({required this.G});
  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        Container(
          width: 1.5 * G,
          height: G,
          color: Colors.red,
        ),
        Positioned(
          top: 0.25 * G,
          left: 0.25 * G,
          child: Container(
            width: 0.5 * G,
            height: 0.5 * G,
            decoration:
                BoxDecoration(color: Colors.white, shape: BoxShape.circle),
          ),
        ),
        Positioned(
          top: 0.3 * G,
          left: 0.3625 * G,
          child: Container(
            width: 0.4 * G,
            height: 0.4 * G,
            decoration:
                BoxDecoration(color: Colors.red, shape: BoxShape.circle),
          ),
        ),
        Positioned(
          top: 0.32 * G,
          left: 0.8 * G,
          child: Container(
            width: 0.25 * G,
            height: 0.25 * G,
            child: Transform(
              transform: Matrix4.rotationZ(1),
              child: Icon(
                Icons.star,
                color: Colors.white,
                size: 0.25 * G,
              ),
            ),
          ),
        ),
      ],
    );
  }
}
