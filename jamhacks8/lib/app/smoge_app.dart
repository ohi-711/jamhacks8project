import 'package:flutter/material.dart';
import 'package:jamhacks8/ui/home_page.dart';

class SmogeApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: HomePage(title: 'Flutter Demo Home Page'),
    );
  }
}