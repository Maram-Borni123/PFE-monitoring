package com.pfe.monitoring_app;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DemoController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello, ton application marche !";
    }

    @GetMapping("/error-test")
    public String error() {
        throw new RuntimeException("Erreur test monitoring");
    }
    @GetMapping("/")
    public String home() {
         return "App Spring Boot OK";
    }
    @GetMapping("/ping")
    public String ping() {
         return "OK";
    }
}
