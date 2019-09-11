classdef EKF
    % FILL IN THE DOTS
    properties
        model
        
        f % discrete prediction function
        F % jacobian of prediction function
        Q % additive discrete noise covariance
        
        h % measurement function
        H % measurement function jacobian
        R % additive measurement noise covariance
    end
    methods 
        function obj = EKF(model)
            obj = obj.setModel(model);
        end
        
        function obj = setModel(obj, model)
           % sets the internal functions from model
           obj.model = model;
           
           obj.f = model.f;
           obj.F = model.F;
           obj.Q = model.Q;
           
           obj.h = model.h;
           obj.H = model.H;
           obj.R = model.R;
        end
        
        function [xp, Pp] = predict(obj, x, P, Ts)
            % returns the predicted mean and covariance for a time step Ts
            Fk = obj.F(x, Ts);
            
            xp = ...
            Pp = ...
        end

        function [vk, Sk] = innovation(obj, z, x, P)
            % returns the innovation and innovation covariance
            Hk = obj.H(x);
            
            vk = ...
            Sk = ...
        end

        function [xupd, Pupd] = update(obj, z, x, P)
            % returns the mean and covariance after conditioning on the
            % measurement
            [vk, Sk] = obj.innovation(z, x, P);
            Hk = obj.H(x);
            I = eye(size(P));
            
            Wk = ...

            xupd = ...
            Pupd = ...
        end

        function NIS = NIS(obj, z, x, P)
            % returns the normalized innovation squared
            [vk, Sk] = obj.innovation(z, x, P);
            
            NIS = ...
        end

        function ll = loglikelihood(obj, z, x, P)
            % returns the logarithm of the marginal mesurement distribution
            [vk, Sk] = obj.innovation(z, x, P);
            NIS = obj.NIS(z, x, P);

            ll = ...
        end

    end
end