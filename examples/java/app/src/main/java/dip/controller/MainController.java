package dip.controller;

import dip.domain.Interface;
import org.springframework.stereotype.Controller;

@Controller
public class MainController {
    Interface inter;

    public MainController(Interface inter) {
        this.inter = inter;
    }

    public void execute() {
        inter.method();
    }
}
