import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {

  HomePage({Key key = const Key(""), this.title = ""}) : super(key: key);

  final String title;
  

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            _buildTitle(),
          ],
        ),
      ),
    );
  }

  Widget _buildTitle() => Text(
        "Wroclaw",
        textAlign: TextAlign.center,
      );
}